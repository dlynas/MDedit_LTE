import sys
import os
import re
import yaml
import json
import logging
import pandas as pd
from collections import Counter, OrderedDict
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QListWidget, 
                             QHBoxLayout, QTextEdit, QLineEdit, QLabel, QMessageBox, QSplitter, QCheckBox, 
                             QListWidgetItem, QGridLayout, QProgressDialog)
from PyQt5.QtGui import QTextCursor, QTextCharFormat, QColor
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QThread, pyqtSignal

# Load stopwords from CSV
stopwords_file_path = 'stopwords.csv'
stopwords = pd.read_csv(stopwords_file_path, header=None)
stopwords_list = stopwords[0].tolist()

# Load CSV files
base_tags_file_path = 'baseTags.csv'
main_tags_file_path = 'mainTags.csv'
triggers_file_path = 'triggers.csv'

base_tags_df = pd.read_csv(base_tags_file_path, header=None)
main_tags_df = pd.read_csv(main_tags_file_path, header=None)
triggers_df = pd.read_csv(triggers_file_path)

# Custom loader and dumper to preserve the order of the YAML keys
def ordered_load(stream, Loader=yaml.SafeLoader, object_pairs_hook=OrderedDict):
    class OrderedLoader(Loader):
        pass
    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))
    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)
    return yaml.load(stream, OrderedLoader)

def ordered_dump(data, stream=None, Dumper=yaml.SafeDumper, **kwds):
    class OrderedDumper(Dumper):
        pass
    def _dict_representer(dumper, data):
        return dumper.represent_dict(data.items())
    OrderedDumper.add_representer(OrderedDict, _dict_representer)
    return yaml.dump(data, stream, OrderedDumper, **kwds)

def loadYAML(yaml_content):
    return ordered_load(yaml_content)

def saveYAML(yaml_data):
    return ordered_dump(yaml_data, default_flow_style=False, allow_unicode=True)

class GlobalKeyFilter(QtCore.QObject):
    def __init__(self, editor, parent=None):
        super().__init__(parent)
        self.editor = editor

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress:
            if event.modifiers() & (QtCore.Qt.ControlModifier | QtCore.Qt.MetaModifier):
                if event.key() == QtCore.Qt.Key_Left:
                    self.editor.selectPreviousFile()
                    return True
                elif event.key() == QtCore.Qt.Key_Right:
                    self.editor.selectNextFile()
                    return True
                elif event.key() == QtCore.Qt.Key_S:  # cmd+s to save file
                    self.editor.saveFile()
                    return True
                elif event.key() == QtCore.Qt.Key_G:  # cmd+g to add selected tag from common words
                    self.editor.addSelectedTag()
                    return True
                elif event.key() == QtCore.Qt.Key_R:  # cmd+r to remove selected tag
                    self.editor.removeSelectedTag()
                    return True
                elif event.key() == QtCore.Qt.Key_T:  # cmd+t to copy tags to frontmatter
                    self.editor.copyTagsToFrontmatter()
                    return True
        return super(GlobalKeyFilter, self).eventFilter(obj, event)

class CustomMarkdownEditor(QTextEdit):
    def __init__(self, parent=None):
        super(CustomMarkdownEditor, self).__init__(parent)

    def highlightLinks(self):
        try:
            text = self.toPlainText()
            cursor = self.textCursor()
            cursor.beginEditBlock()
            local_link_format = QTextCharFormat()
            local_link_format.setForeground(QColor("green"))
            broken_link_format = QTextCharFormat()
            broken_link_format.setForeground(QColor("red"))
            web_link_format = QTextCharFormat()
            web_link_format.setForeground(QColor("orange"))

            self.setUpdatesEnabled(False)
            patterns = [
                r'\[([^\]]+)\]\((https?://[^\s\)]+)\)',
                r'(https?://[^\s\)]+)',
                r'\[\[([^\]]+)\]\]',
                r'!\[\[([^\]]+)\]\]',  # Embedded file pattern
                r'!\[\]\(([^)]+)\)'  # Local file pattern
            ]

            for pattern in patterns:
                matches = re.finditer(pattern, text)
                for match in matches:
                    cursor.setPosition(match.start(), QTextCursor.MoveAnchor)
                    cursor.setPosition(match.end(), QTextCursor.KeepAnchor)
                    if pattern == patterns[0] or pattern == patterns[1]:
                        cursor.setCharFormat(web_link_format)
                    elif pattern == patterns[3] or pattern == patterns[4]:
                        local_path = match.group(1)
                        if self.isLinkBroken(local_path, embedded=True):
                            cursor.setCharFormat(broken_link_format)
                        else:
                            cursor.setCharFormat(local_link_format)
                            if local_path.endswith('.md'):
                                self.embedMarkdown(cursor, local_path)
                            else:
                                self.embedMedia(cursor, local_path)
                    else:
                        local_path = match.group(1)
                        if self.isLinkBroken(local_path):
                            cursor.setCharFormat(broken_link_format)
                        else:
                            cursor.setCharFormat(local_link_format)
            cursor.endEditBlock()
            self.setUpdatesEnabled(True)
        except Exception as e:
            self.showErrorMessage(str(e))

    def isLinkBroken(self, link, embedded=False):
        try:
            base_paths = [
                './_notes/', 
                './_metamedia/', 
                './_metamedia/local/', 
                './_resources/video/', 
                './_resources/images/'
            ]
            if not link.endswith('.md') and embedded:
                link_with_extension = link + '.md'
            else:
                link_with_extension = link

            for base_path in base_paths:
                for root, dirs, files in os.walk(base_path):
                    if link in files or link_with_extension in files:
                        return False
            return True
        except Exception as e:
            self.showErrorMessage(str(e))
            return True

    def embedMedia(self, cursor, local_path):
        try:
            original_position = cursor.position()
            file_path = self.findMediaFile(local_path)
            if file_path:
                if file_path.endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    img_tag = f'<img src="{file_path}" alt="Image" width="400">'
                    cursor.movePosition(QTextCursor.EndOfLine)
                    cursor.insertHtml(f'<br>{img_tag}<br>')
                elif file_path.endswith(('.mp4', '.webm')):
                    video_tag = f'<video width="400" controls><source src="{file_path}" type="video/mp4">Your browser does not support the video tag.</video>'
                    cursor.movePosition(QTextCursor.EndOfLine)
                    cursor.insertHtml(f'<br>{video_tag}<br>')
            cursor.setPosition(original_position, QTextCursor.MoveAnchor)
        except Exception as e:
            self.showErrorMessage(str(e))

    def embedMarkdown(self, cursor, markdown_path):
        try:
            full_path = self.findMarkdownFile(markdown_path)
            if full_path:
                with open(full_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                cursor.insertText("\n" + content + "\n")
                self.highlightLinks()
                self.parent().updateWordFrequency(content)
                self.parent().autoSelectTags(content)
        except Exception as e:
            self.showErrorMessage(str(e))

    def findMediaFile(self, link):
        base_paths = [
            './_notes/', 
            './_metamedia/', 
            './_metamedia/local/', 
            './_resources/video/', 
            './_resources/images/'
        ]
        for base_path in base_paths:
            for root, dirs, files in os.walk(base_path):
                if link in files:
                    return os.path.join(root, link)
        return None

    def findMarkdownFile(self, link):
        if not link.endswith('.md'):
            link += '.md'
        base_paths = [
            './_notes/', 
            './_metamedia/', 
            './_metamedia/local/', 
            './_resources/video/', 
            './_resources/images/'
        ]
        for base_path in base_paths:
            for root, dirs, files in os.walk(base_path):
                if link in files:
                    return os.path.join(root, link)
        return None

    def keyPressEvent(self, event):
        super(CustomMarkdownEditor, self).keyPressEvent(event)

    def showErrorMessage(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("An error occurred")
        msg.setInformativeText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

class MarkdownEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.last_search_pos = 0
        self.current_file_path = None
        self.file_modified = False
        self.loaded_files = []  # Store the list of loaded files

    def initUI(self):
        main_splitter = QSplitter(Qt.Horizontal)

        # Left side - File Browser and Open Folder button
        left_splitter = QSplitter(Qt.Vertical)

        # Add search bar
        search_layout = QVBoxLayout()
        self.searchInput = QLineEdit()
        self.searchInput.setPlaceholderText("Search files")
        self.searchInput.textChanged.connect(self.searchFiles)
        search_layout.addWidget(self.searchInput)

        self.fileList = QListWidget()
        self.fileList.itemClicked.connect(self.loadSelectedFile)
        search_layout.addWidget(self.fileList)

        search_widget = QWidget()
        search_widget.setLayout(search_layout)
        
        self.openFolderButton = QPushButton('Open Folder')
        self.openFolderButton.clicked.connect(self.openFolder)
        left_splitter.addWidget(search_widget)
        left_splitter.addWidget(self.openFolderButton)

        main_splitter.addWidget(left_splitter)

        # Center section - YAML Editor, Tag Input, Markdown Editor, Save File button
        center_splitter = QSplitter(Qt.Vertical)

        self.yamlEditor = QTextEdit()
        self.yamlEditor.setPlaceholderText("YAML Frontmatter")
        self.yamlEditor.textChanged.connect(self.markAsModified)
        center_splitter.addWidget(self.yamlEditor)

        # New widget to display embeds.json content
        self.embeddedContentDisplay = QTextEdit()  # Corrected the name here
        self.embeddedContentDisplay.setPlaceholderText("Embedded Markdown Texts")
        self.embeddedContentDisplay.setReadOnly(True)  # Make it read-only
        center_splitter.addWidget(self.embeddedContentDisplay)

        tagInputWidget = QWidget()
        tagInputLayout = QHBoxLayout()
        self.tagInput = QLineEdit()
        self.tagInput.setPlaceholderText('Enter a tag')
        self.addTagButton = QPushButton('Add Tag')
        self.addTagButton.clicked.connect(self.addTag)
        tagInputLayout.addWidget(self.tagInput)
        tagInputLayout.addWidget(self.addTagButton)
        tagInputWidget.setLayout(tagInputLayout)
        center_splitter.addWidget(tagInputWidget)

        self.editor = CustomMarkdownEditor()
        self.editor.textChanged.connect(self.markAsModified)
        center_splitter.addWidget(self.editor)

        self.saveButton = QPushButton('Save File')
        self.saveButton.clicked.connect(self.saveFile)
        self.saveButton.setToolTip("Cmd+S - Save File")  # Tooltip for Save File button
        center_splitter.addWidget(self.saveButton)

        main_splitter.addWidget(center_splitter)


        # Right side - Tagging and Tags
        right_splitter = QSplitter(Qt.Vertical)
        
        self.wordList = QListWidget()
        self.populateListWidget(self.wordList, columns=3)  # Adjust columns as needed
        right_splitter.addWidget(self.wordList)
        
        self.addSelectedTagButton = QPushButton('Add Selected as Tag')
        right_splitter.addWidget(self.addSelectedTagButton)
        self.addSelectedTagButton.setToolTip("Cmd+G - Add Selected Tag from Common Words")  # Tooltip for Add Selected Tag button
        self.addSelectedTagButton.clicked.connect(self.addSelectedTag)

        tags_layout = QGridLayout()
        
        # Inside the initUI method, initialize the fileTags and baseTags list widgets
        self.fileTags = QListWidget()
        self.populateListWidget(self.fileTags, columns=3)  # Adjust columns as needed
        tags_layout.addWidget(QLabel("File Tags"), 0, 0)
        tags_layout.addWidget(self.fileTags, 1, 0)

        self.baseTags = QListWidget()
        self.populateListWidget(self.baseTags, columns=3)  # Adjust columns as needed
        tags_layout.addWidget(QLabel("Base Tags"), 0, 1)
        tags_layout.addWidget(self.baseTags, 1, 1)

        self.allTags = QListWidget()
        self.populateListWidget(self.allTags, columns=3)  # Adjust columns as needed
        tags_layout.addWidget(QLabel("All Tags"), 0, 2)
        tags_layout.addWidget(self.allTags, 1, 2)
        
        tags_widget = QWidget()
        tags_widget.setLayout(tags_layout)
        right_splitter.addWidget(tags_widget)

        self.removeTagButton = QPushButton('Remove Selected Tag')
        self.removeTagButton.clicked.connect(self.removeSelectedTag)
        self.removeTagButton.setToolTip("Cmd+R - Remove Selected Tag")  # Tooltip for Remove Selected Tag button
        right_splitter.addWidget(self.removeTagButton)
        
        # Adding baseTags and mainTags sections
        self.baseTagsWidget = self.createTagWidget(base_tags_df, 'Base Tags', 'red', columns=5)
        right_splitter.addWidget(self.baseTagsWidget)

        self.mainTagsWidget = self.createTagWidget(main_tags_df, 'Main Tags', 'red', columns=5)
        right_splitter.addWidget(self.mainTagsWidget)

        self.copyTagsButton = QPushButton('Copy Selected Tags to Frontmatter')
        self.copyTagsButton.clicked.connect(self.copyTagsToFrontmatter)
        self.copyTagsButton.setToolTip("Cmd+T - Copy Selected Tags to Frontmatter")  # Tooltip for Copy Tags to Frontmatter button
        right_splitter.addWidget(self.copyTagsButton)
        self.processTagsButton = QPushButton('All Tags to All Files')
        self.processTagsButton.clicked.connect(self.processTagsForAllFiles)
        right_splitter.addWidget(self.processTagsButton)

        
        main_splitter.addWidget(right_splitter)

        layout = QHBoxLayout()
        layout.addWidget(main_splitter)
        self.setLayout(layout)
        self.setWindowTitle('Markdown Editor')

        self.globalKeyFilter = GlobalKeyFilter(self)
        self.installEventFilter(self.globalKeyFilter)

    def populateListWidget(self, widget, columns=3):
        widget.setViewMode(QListWidget.IconMode)
        widget.setWrapping(True)
        widget.setGridSize(QtCore.QSize(150, 20))
        widget.setSpacing(5)
        widget.setResizeMode(QListWidget.Adjust)
        widget.setSelectionMode(QListWidget.MultiSelection)  # Allow multiple selections


    def createTagWidget(self, tags_df, label, color, columns=5):
        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel(label))
        
        grid_layout = QGridLayout()
        row = 0
        col = 0
        for index, row_data in tags_df.iterrows():
            for tag in row_data.dropna():
                checkbox = QCheckBox(tag)
                checkbox.setStyleSheet(f"background-color: {color};")
                grid_layout.addWidget(checkbox, row, col)
                col += 1
                if col >= columns:
                    col = 0
                    row += 1

        layout.addLayout(grid_layout)
        widget.setLayout(layout)
        return widget


    def processTagsForAllFiles(self):
        if not self.loaded_files:
            QMessageBox.information(self, "No Files", "No files loaded in the browser to process.")
            return

        confirm = QMessageBox.question(self, "Confirm", "Are you sure you want to process tags for all loaded files?",
                                    QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.No:
            return

        self.progress_dialog = QProgressDialog("Processing files...", "Pause", 0, len(self.loaded_files), self)
        self.progress_dialog.setWindowTitle("Processing Tags")
        self.progress_dialog.setWindowModality(Qt.WindowModal)
        self.progress_dialog.setMinimumDuration(0)

        self.progress_dialog.canceled.connect(self.pauseProcessing)

        self.current_processing_index = 0
        self.paused = False

        self.processNextFile()

    def processNextFile(self):
        if self.current_processing_index >= len(self.loaded_files):
            QMessageBox.information(self, "Completed", "Tagging process completed for all files.")
            return

        if self.paused:
            return

        file, full_path = self.loaded_files[self.current_processing_index]

        self.loadFileForProcessing(full_path)
        self.autoSelectTags(self.editor.toPlainText())
        self.saveFile()

        self.current_processing_index += 1
        self.progress_dialog.setValue(self.current_processing_index)

        if self.current_processing_index < len(self.loaded_files):
            QtCore.QTimer.singleShot(100, self.processNextFile)
        else:
            QMessageBox.information(self, "Completed", "Tagging process completed for all files.")

    def pauseProcessing(self):
        if self.progress_dialog.wasCanceled():
            self.paused = True
            resume = QMessageBox.question(self, "Paused", "Process paused. Do you want to resume?",
                                        QMessageBox.Yes | QMessageBox.No)
            if resume == QMessageBox.Yes:
                self.paused = False
                self.processNextFile()



    def loadFileForProcessing(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            self.editor.setPlainText(content)
            self.editor.highlightLinks()
            yaml_frontmatter = self.extractYAMLFrontmatter(content)
            self.yamlEditor.setPlainText(saveYAML(yaml_frontmatter))
            self.current_file_path = file_path
            self.file_modified = False
        except Exception as e:
            logging.error(f"Error loading file {file_path}: {str(e)}")
            self.showErrorMessage(str(e))




    def copyTagsToFrontmatter(self):
        selected_base_tags = self.getSelectedTags(self.baseTagsWidget)
        selected_main_tags = self.getSelectedTags(self.mainTagsWidget)

        yaml_content = self.yamlEditor.toPlainText()
        yaml_data = loadYAML(yaml_content) if yaml_content.strip() else {}

        base_tags = yaml_data.get('base_tags', '').split(', ')
        main_tags = yaml_data.get('tags', '').split(', ')

        base_tags = list(filter(None, base_tags))  # Remove empty strings
        main_tags = list(filter(None, main_tags))

        new_tags_added = False
        for tag in selected_base_tags:
            if tag not in base_tags:
                base_tags.append(tag)
                new_tags_added = True

        for tag in selected_main_tags:
            if tag not in main_tags:
                main_tags.append(tag)
                new_tags_added = True

        if new_tags_added:
            yaml_data['base_tags'] = ', '.join(sorted(base_tags))
            yaml_data['tags'] = ', '.join(sorted(main_tags))

            updated_yaml_content = saveYAML(yaml_data)
            self.yamlEditor.setPlainText(updated_yaml_content)

            self.updateTagDisplay()  # Ensure the tag display is updated correctly

            for tag in selected_base_tags + selected_main_tags:
                self.updateAllTags(tag, increment=True)  # Update All Tags count

            self.populateAllTagsList()
            self.markAsModified()

    def getSelectedTags(self, widget):
        selected_tags = []
        for checkbox in widget.findChildren(QCheckBox):
            if checkbox.isChecked():
                selected_tags.append(checkbox.text())
        return selected_tags

    def closeEvent(self, event):
        if self.file_modified:
            reply = QMessageBox.question(self, 'Save Changes',
                                        "You have unsaved changes. Would you like to save them?",
                                        QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if reply == QMessageBox.Yes:
                self.saveFile()
            if reply != QMessageBox.Cancel:
                QApplication.quit()
                event.accept()
            else:
                event.ignore()
        else:
            QApplication.quit()
            event.accept()

    def removeSelectedTag(self):
        selectedFileTags = self.fileTags.selectedItems()
        selectedBaseTags = self.baseTags.selectedItems()
        selectedItems = selectedFileTags + selectedBaseTags  # Include baseTags

        if selectedItems:
            selectedTag = selectedItems[0].text()
            yaml_content = self.yamlEditor.toPlainText()
            yaml_data = loadYAML(yaml_content) if yaml_content.strip() else {}

            tags = yaml_data.get('tags', '').split(', ')
            base_tags = yaml_data.get('base_tags', '').split(', ')

            tag_removed_from_file_tags = False
            tag_removed_from_base_tags = False

            if 'tags' in yaml_data and selectedTag in tags:
                tags.remove(selectedTag)
                yaml_data['tags'] = ', '.join(tags)
                tag_removed_from_file_tags = True

            if 'base_tags' in yaml_data and selectedTag in base_tags:
                base_tags.remove(selectedTag)
                yaml_data['base_tags'] = ', '.join(base_tags)
                tag_removed_from_base_tags = True

            if tag_removed_from_file_tags or tag_removed_from_base_tags:
                updated_yaml_content = saveYAML(yaml_data)
                self.yamlEditor.setPlainText(updated_yaml_content)

                self.updateTagLists(tags, base_tags)

                # Update the count correctly
                decrement_count = 0
                if tag_removed_from_file_tags:
                    decrement_count += 1
                if tag_removed_from_base_tags:
                    decrement_count += 1

                self.updateAllTags(selectedTag, increment=False, count=decrement_count)
                self.populateAllTagsList()
                self.markAsModified()

    def markAsModified(self):
        self.file_modified = True

    def promptSaveChanges(self):
        if self.file_modified:
            reply = QMessageBox.question(self, 'Save Changes',
                                         "You have unsaved changes. Would you like to save them?",
                                         QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if reply == QMessageBox.Yes:
                self.saveFile()
            elif reply == QMessageBox.Cancel:
                return False
        return True

    def loadSelectedFile(self, item):
        if not self.promptSaveChanges():
            return
        try:
            # Retrieve the full path from the item's data
            full_path = item.data(Qt.UserRole)
            if full_path:
                with open(full_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                self.editor.setPlainText(content)
                self.editor.highlightLinks()
                self.updateWordFrequency(content)
                yaml_frontmatter = self.extractYAMLFrontmatter(content)
                self.yamlEditor.setPlainText(saveYAML(yaml_frontmatter))
                self.file_modified = False
                self.populateAllTagsList()

                main_tags = yaml_frontmatter.get('tags', '').split(', ')
                main_tags.sort()
                base_tags = yaml_frontmatter.get('base_tags', '').split(', ')
                base_tags.sort()

                self.updateTagLists(main_tags, base_tags)
                self.autoSelectTags(content)
                self.current_file_path = full_path

                # Load embedded markdown files
                self.loadEmbeddedMarkdownFiles(content)

                # Update the new QTextEdit widget with embedded content
                self.updateEmbeddedContentDisplay()

        except Exception as e:
            logging.error(f"Error loading file {full_path}: {str(e)}")
            self.showErrorMessage(str(e))

    def loadEmbeddedMarkdownFiles(self, content):
        pattern = re.compile(r'!\[\[([^\]]+)\]\]')
        matches = pattern.findall(content)

        embedded_texts = []
        for match in matches:
            if not match.endswith('.md'):
                match += '.md'
            file_path = self.editor.findMarkdownFile(match)
            if file_path:
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        embedded_text = file.read()
                        embedded_texts.append(embedded_text)
                except Exception as e:
                    logging.error(f"Error loading embedded file {file_path}: {str(e)}")

        cleaned_texts = [self.cleanText(text) for text in embedded_texts]
        combined_text = ' '.join(cleaned_texts)

        with open('embeds.json', 'w', encoding='utf-8') as json_file:
            json.dump({"embedded_texts": combined_text}, json_file, ensure_ascii=False, indent=4)

        self.analyzeEmbeddedContent(combined_text)

    def analyzeEmbeddedContent(self, combined_text):
        self.updateWordFrequency(combined_text, is_embedded=True)
        self.autoSelectTags(combined_text, is_embedded=True)

    def cleanText(self, text):
        text = re.sub(r'\W+', ' ', text).lower()
        return text

    def updateEmbeddedContentDisplay(self):
        try:
            with open('embeds.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                embedded_text = data.get('embedded_texts', '')
            self.embeddedContentDisplay.setPlainText(embedded_text)
        except Exception as e:
            logging.error(f"Error loading embedded content display: {str(e)}")
            self.showErrorMessage(str(e))


    def updateWordFrequency(self, content, is_embedded=False):
        words = re.findall(r'\b\w+\b', content)
        freq = Counter(words)
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        if not is_embedded:
            self.wordList.clear()
        for word, count in sorted_freq:
            if 3 <= len(word) <= 15 and word.lower() not in stopwords_list: 
                if is_embedded:
                    self.wordList.addItem(f"{word}")
                else:
                    self.wordList.addItem(word)

    def autoSelectTags(self, content, is_embedded=False):
        triggers = pd.read_csv('triggers.csv')
        trigger_dict = {row['Trigger'].lower(): row['Keywords'].split(', ') for index, row in triggers.iterrows()}
        words = content.split()
        selected_keywords = set()
        for word in words:
            if word.lower() in trigger_dict:
                selected_keywords.update(trigger_dict[word.lower()])
        if is_embedded:
            self.updateTagSelections(selected_keywords, is_embedded=True)
        else:
            self.updateTagSelections(selected_keywords)

    def updateTagSelections(self, selected_keywords, is_embedded=False):
        for checkbox in self.baseTagsWidget.findChildren(QCheckBox):
            if is_embedded:
                if checkbox.text() in selected_keywords and not checkbox.isChecked():
                    checkbox.setChecked(True)
            else:
                checkbox.setChecked(checkbox.text() in selected_keywords)
        for checkbox in self.mainTagsWidget.findChildren(QCheckBox):
            if is_embedded:
                if checkbox.text() in selected_keywords and not checkbox.isChecked():
                    checkbox.setChecked(True)
            else:
                checkbox.setChecked(checkbox.text() in selected_keywords)


    def selectPreviousFile(self):
        if not self.promptSaveChanges():
            return
        current_row = self.fileList.currentRow()
        if current_row > 0:
            self.fileList.setCurrentRow(current_row - 1)
            self.loadSelectedFile(self.fileList.currentItem())
            self.populateAllTagsList()

    def selectNextFile(self):
        if not self.promptSaveChanges():
            return
        current_row = self.fileList.currentRow()
        if current_row < self.fileList.count() - 1:
            self.fileList.setCurrentRow(current_row + 1)
            self.loadSelectedFile(self.fileList.currentItem())
            self.populateAllTagsList()

    def saveFile(self):
        try:
            if not self.current_file_path:
                options = QFileDialog.Options()
                fileName, _ = QFileDialog.getSaveFileName(self, "Save Markdown File", "", "Markdown Files (*.md);;All Files (*)", options=options)
                if not fileName:
                    return
                self.current_file_path = fileName

            content = self.editor.toPlainText()
            yaml_frontmatter = self.yamlEditor.toPlainText()
            yaml_data = loadYAML(yaml_frontmatter) if yaml_frontmatter.strip() else {}

            if yaml_data:
                yaml_frontmatter = '---\n' + saveYAML(yaml_data).strip() + '\n---\n'
            else:
                yaml_frontmatter = ''

            content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
            content = yaml_frontmatter + content

            with open(self.current_file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            self.file_modified = False
            self.populateAllTagsList()

            # Clear embeds.json
            with open('embeds.json', 'w', encoding='utf-8') as json_file:
                json.dump({"embedded_texts": ""}, json_file, ensure_ascii=False, indent=4)

            logging.info(f"File saved: {self.current_file_path}")
        except Exception as e:
            logging.error(f"Error saving file {self.current_file_path}: {str(e)}")
            self.showErrorMessage(str(e))

    def keyPressEvent(self, event):
        modifiers = event.modifiers()
        key = event.key()
        if modifiers & Qt.ControlModifier:
            if key == Qt.Key_Left:
                self.selectPreviousFile()
            elif key == Qt.Key_Right:
                self.selectNextFile()
        super().keyPressEvent(event)

    def loadFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Markdown File", "", "Markdown Files (*.md);;All Files (*)", options=options)
        if fileName:
            try:
                with open(fileName, 'r', encoding='utf-8') as file:
                    content = file.read()
                self.editor.setPlainText(content)
                self.editor.highlightLinks()
                yaml_frontmatter = self.extractYAMLFrontmatter(content)
                self.yamlEditor.setPlainText(saveYAML(yaml_frontmatter))
                self.current_file_path = fileName
                self.file_modified = False
                self.populateAllTagsList()

                # Load embedded markdown files
                self.loadEmbeddedMarkdownFiles(content)
            except Exception as e:
                logging.error(f"Error loading file {fileName}: {str(e)}")
                self.showErrorMessage(str(e))

    def openFolder(self):
        try:
            options = QFileDialog.Options()
            folder = QFileDialog.getExistingDirectory(self, "Select Folder", options=options)
            if folder:
                self.loadFolder(folder)
        except Exception as e:
            logging.error(f"Error opening folder: {str(e)}")
            self.showErrorMessage(str(e))

    def loadFolder(self, folder):
        self.fileList.clear()
        self.loaded_files = []
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.endswith(".md"):
                    full_path = os.path.join(root, file)
                    self.loaded_files.append((file, full_path))
        
        # Sort files alphabetically by filename
        self.loaded_files.sort(key=lambda x: x[0])
        
        self.updateFileList(self.loaded_files)

    def updateFileList(self, files):
        self.fileList.clear()
        for file, full_path in files:
            item = QListWidgetItem(file)
            item.setData(QtCore.Qt.UserRole, full_path)  # Store the full path
            self.fileList.addItem(item)

    def searchFiles(self):
        query = self.searchInput.text().lower()
        filtered_files = []
        for file, full_path in self.loaded_files:
            if query in file.lower() or self.fileContainsText(full_path, query):
                filtered_files.append((file, full_path))
        self.updateFileList(filtered_files)

    def fileContainsText(self, file_path, text):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read().lower()
                return text in content
        except Exception as e:
            logging.error(f"Error reading file {file_path} for search: {str(e)}")
            return False

    def replaceText(self):
        try:
            cursor = self.editor.textCursor()
            replace = self.replaceInput.text()

            if cursor.hasSelection():
                cursor.insertText(replace)
                self.editor.setTextCursor(cursor)
                self.selectNextOccurrence(self.searchInput.text())
        except Exception as e:
            logging.error(f"Error replacing text: {str(e)}")
            self.showErrorMessage(str(e))

    def replaceAllText(self):
        try:
            text = self.editor.toPlainText()
            search = self.searchInput.text()
            replace = self.replaceInput.text()
            updated_text = text.replace(search, replace)
            self.editor.setPlainText(updated_text)
            self.editor.highlightLinks()
        except Exception as e:
            logging.error(f"Error replacing all text: {str(e)}")
            self.showErrorMessage(str(e))

    def addSelectedTag(self):
        selectedItems = self.wordList.selectedItems()
        if selectedItems:
            yaml_content = self.yamlEditor.toPlainText()
            yaml_data = loadYAML(yaml_content) if yaml_content.strip() else {}

            if 'tags' not in yaml_data or not isinstance(yaml_data['tags'], str):
                yaml_data['tags'] = ''

            tags = yaml_data['tags'].split(', ') if yaml_data['tags'] else []

            new_tags = []
            for item in selectedItems:
                cleanedText = re.sub('[^a-zA-Z]', '', item.text()).lower()
                if cleanedText not in tags and cleanedText:
                    new_tags.append(cleanedText)
                    tags.append(cleanedText)

            if new_tags:
                tags.sort()
                yaml_data['tags'] = ', '.join(tags)
                updated_yaml_content = saveYAML(yaml_data)
                self.yamlEditor.setPlainText(updated_yaml_content)
                self.updateTagLists(tags, self.getTagsList(self.baseTags))
                for tag in new_tags:
                    self.updateAllTags(tag)
                self.populateAllTagsList()
                self.markAsModified()


    def updateTagLists(self, main_tags=None, base_tags=None):
        self.fileTags.clear()
        self.baseTags.clear()
        if main_tags is not None:
            for tag in main_tags:
                self.fileTags.addItem(QListWidgetItem(tag))
        if base_tags is not None:
            for tag in base_tags:
                self.baseTags.addItem(QListWidgetItem(tag))

    def loadAllTags(self):
        try:
            with open('all_tags.json', 'r') as file:
                tags = json.load(file)
                return tags if isinstance(tags, dict) else {}
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def saveAllTags(self, tags):
        with open('all_tags.json', 'w') as file:
            json.dump(tags, file, indent=2)

    def updateAllTags(self, tag, increment=True, count=1):
        all_tags = self.loadAllTags()
        tag = tag.lower()

        if increment:
            if tag in all_tags:
                all_tags[tag] += count
            else:
                all_tags[tag] = count
        else:
            if tag in all_tags:
                all_tags[tag] -= count
                if all_tags[tag] <= 0:
                    del all_tags[tag]

        self.saveAllTags(all_tags)
        self.populateAllTagsList()

    def populateAllTagsList(self):
        all_tags = self.loadAllTags()
        sorted_tags = sorted(all_tags.keys())
        self.allTags.clear()
        for tag in sorted_tags:
            item = QListWidgetItem(f"{tag} ({all_tags[tag]})")
            self.allTags.addItem(item)

    def wordFrequencyAnalysis(self):
        try:
            text = self.editor.toPlainText()
            words = re.findall(r'\w+', text.lower())
            freq = Counter(words)
            sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
            result = '\n'.join([f'{word}: {count}' for word, count in sorted_freq])
            self.showFrequencyResult(result)
        except Exception as e:
            logging.error(f"Error in word frequency analysis: {str(e)}")
            self.showErrorMessage(str(e))

    def showFrequencyResult(self, result):
        try:
            resultDialog = QWidget()
            resultDialog.setWindowTitle('Word Frequency Analysis')
            layout = QVBoxLayout()
            resultText = QTextEdit()
            resultText.setPlainText(result)
            layout.addWidget(resultText)
            resultDialog.setLayout(layout)
            resultDialog.show()
        except Exception as e:
            logging.error(f"Error showing frequency result: {str(e)}")
            self.showErrorMessage(str(e))

    def extractYAMLFrontmatter(self, text):
        try:
            match = re.match(r'^---\n(.*?)\n---', text, re.DOTALL)
            if match:
                return loadYAML(match.group(1))
            return {}
        except Exception as e:
            logging.error(f"Error extracting YAML frontmatter: {str(e)}")
            self.showErrorMessage(str(e))
            return {}

    def addTag(self):
        tag = self.tagInput.text().strip().lower()
        if not tag:
            return

        yaml_content = self.yamlEditor.toPlainText()
        yaml_data = loadYAML(yaml_content) if yaml_content.strip() else {}

        if 'tags' not in yaml_data:
            yaml_data['tags'] = ""

        existing_tags = [existing_tag.strip() for existing_tag in yaml_data['tags'].split(",") if existing_tag.strip()]
        
        if tag not in existing_tags:
            existing_tags.append(tag)
            existing_tags.sort()
            yaml_data['tags'] = ", ".join(existing_tags)
            updated_yaml_content = saveYAML(yaml_data)
            self.yamlEditor.setPlainText(updated_yaml_content)

            self.updateTagLists(existing_tags, self.getTagsList(self.baseTags))
            self.updateAllTags(tag)
            self.populateAllTagsList()
            self.markAsModified()

            self.tagInput.clear()
        else:
            QMessageBox.information(self, "Duplicate Tag", "This tag is already added.")

    def getTagsList(self, widget):
        tags = []
        for index in range(widget.count()):
            item = widget.item(index)
            tags.append(item.text())
        return tags

    def showErrorMessage(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("An error occurred")
        msg.setInformativeText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

if __name__ == '__main__':
    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ])

    app = QApplication(sys.argv)  # Create the application object
    try:
        editor = MarkdownEditor()  # Initialize your main window class
        globalKeyFilter = GlobalKeyFilter(editor)  # Create a global key filter and apply it to the editor
        app.installEventFilter(globalKeyFilter)  # Install the global key filter on the application
        editor.show()  # Show the main window
        exit_code = app.exec_()  # Run the application's event loop
        sys.exit(exit_code)  # Ensure a clean exit with the exit code from the application
    except Exception as e:
        logging.critical(f"Critical error on startup: {str(e)}", exc_info=True)  # Log the error with stack trace
        error_msg = QMessageBox()  # Create a message box to show the error
        error_msg.setIcon(QMessageBox.Critical)
        error_msg.setText("An error occurred during startup")
        error_msg.setInformativeText(str(e))
        error_msg.setWindowTitle("Startup Error")
        error_msg.exec_()  # Display the error message box
        sys.exit(1)  # Exit the application with an error code
