---
source: hci.stanford.edu
url: https://hci.stanford.edu/winograd/papers/language-action.html
---

Three points deserve note:

1) The illocutionary point of an utterance is interpreted by speaker and hearer in a background. A commissive need not include the words I promise or I will, but can be I guess or a dollar (in response to Can you give me anything?) or just a facial gesture. The identification of a language act depends on the backgrounds of speaker and hearer, and is always open to differences of interpretation. Its time for lunch might be an assertive or a directive, depending on who says it to whom in what circumstances.

2) Directives and commissives (which will informally be called requests and promises here) always deal with a future action. They differ in whether the action is to be taken by the speaker or the hearer.

3) Speech acts take effect by virtue of public declaration -- by mutual knowledge of hearer and speaker that the act has been made. This is especially obvious in the case of declarations and expressives (e.g., an apology muttered but not heard is not an apology), but is equally true of the others.

#### 3.2. Conversations for action

Speech acts are not unrelated events, but participate in larger conversation structures (Flores, 1981; Flores and Ludlow, 1981). An important example is the simple conversation for action, in which one party (A) makes a request to another (B). The request is interpreted by each party as having certain conditions of satisfaction, which characterize a future course of actions by B. After the initial utterance (the request), B can accept (and thereby commit to satisfy the conditions); decline (and thereby end the conversation); or counter-offer with alternative conditions. Each of these in turn has its possible continuations (e.g., after a counter-offer, A can accept, cancel the request, or counter-offer back). The overall structure is diagrammed in Figure 1.

> _Figure 1. \[Not yet included on line\] State transition network representing a conversation for action initiated by a request from speaker A to speaker B. The circles represent conversation states and the labelled lines represent speech acts. Heavy circles represent states of completion. (adapted from Winograd and Flores, 1986, p. 65.)_

This diagram is not a model of the mental state of a speaker or hearer, but shows the conversation as a dance, in which the conversation steps proceed towards mutual recognition that the requested action has been done or that the conversation is complete without it having been done. The basic logic represented here deals with the central progression of acts. Other possibilities not shown in the diagram can emerge in related conversations, such as those in which the conversational acts themselves are taken as a topic. For example, a speaker might question intelligibility (What, I didnt hear you) or legitimacy (You cant order me to do that!).

If B commits to fulfill a request (moving to state 3), the natural continuation is that at some later point B reports to A that the conditions of satisfaction have been met (moving to state 4). If A declares that he or she is satisfied, the conversation reaches a successful completion (state 5). On the other hand, A may not interpret the situation in the same way and may decline the report, declaring that the conditions have not been met and thereby returning the conversation to state 3. In any state, either party may propose changes to the conditions of satisfaction or may back out on the deal, moving to a state of completion (7 and 9) that does not include satisfaction of the original request.

Several points about this conversation structure deserve note:

1) We use conversation in a very general sense to indicate a coordinated sequence of acts that can be interpreted as having linguistic meaning. It need not be a spoken conversation, or even involve the use of ordinary language. A doctor who writes treatment requests on a patient form is engaged in a conversation with the nurse who will administer the treatments, even if they never speak face-to-face. Certain kinds of requests are made implicitly on the basis of a long-term declaration. A manager does not explicitly request each worker to come to work each morning, although the conversation proceeds (in those cases where there is a breakdown) as though he or she had. The recurrent request is listened to as an effect of the declaration Youre hired within a shared understanding of common practices.

2) The conversation is initiated by a request (there is a similar network for conversations initiated by an offer), and therefore is rooted in the anticipation of some future action.

3) At each point in the conversation, there is a small set of possible action types, determined by the previous history. Each type has unlimited possibilities for detailed content. For example, a counter-offer action specifies particular conditions of satisfaction.

4) All of the acts are linguistic -- they represent utterances by parties to the conversation (or silences that are listened to as standing for an act). For example, the act that normally follows a promise is a report of completion (an assertive speech act) from the promisor to the requestor. It is followed by a declaration by the requestor that that the action is satisfactory (or that it is not). The actual doing of whatever is needed to meet the conditions of satisfaction lies outside of the conversation structure.

5) Many acts are listened to without being explicit. If the requestor can recognize satisfaction of the request directly, there may be no explicit report of completion. Other acts, such as declaring satisfaction, may be taken for granted if some amount of time goes by without a communication to the contrary. What is not said is listened to as much as what is said.

6) Conditions of satisfaction are not objective realities, independent of interpretations. They exist in the listening, and there is always the potential for difference among the parties. This can lead to breakdowns and to subsequent conversation about the understanding of the conditions.

7) There are states of completion (the heavy circles in the figure) in which it is mutually recognized that neither party is waiting for further action by the other. All other states represent an incomplete conversation. Completion does not guarantee satisfaction. For example, if the promisor cancels after the promise is made, the conversation is completed without the original request being satisfied.

8) The network does not say what people should do, or deal with consequences of their acts (such as backing out of a commitment). These are important human phenomena, but are not generated in the domain formalized in this network. Conversations for action are the central coordinating structure for human organizations. We work together by making commitments so that we can successfully anticipate the actions of others and coordinate them with our own. The emphasis here is on language as an activity, not as the transmission of information or as the expression of thought. Although people think when they use language, and they often describe their world in language, the relevant structures for analysis here are the language acts and the conversations into which they are woven. In applying this to computer system design, we are not concerned with duplicating the knowledge or thought patterns of people, but with the structure of their interactions and the embedding of those interactions in computer systems.

### 4\. Designing conversations for action

We will illustrate the relevance of this analysis to computer systems, by describing The Coordinator1, a first-generation conversational system currently used for everyday communications in sales, finance, general management, operations, and planning functions in organizations of a variety of sizes and types. This system provides facilities for generating, transmitting, storing, retrieving and displaying messages that are records of moves in conversations. However, unlike electronic mail systems that take messages and information as their starting points, it is based on the conversation theory outlined above.

#### 4.1. Tools for conversing

The user interface of The Coordinator is menu driven. The primary menu for conversing is shown in Figure 2. Some of the menu items indicate new actions the user may take. Others bring up displays of the records of conversations maintained by the system. Let us look first at ways of opening a conversation for action (answering is discussed below, and conversations for possibilities will be discussed in the Section 5).

Rather than providing a uniform command to initiate a new message, The Coordinator system provides options for opening conversations that have different implicit structures of action. When Request is selected, templates appear prompting the user to specify an addressee, others who will receive copies, a domain, which groups or categorizes related conversations, and an action description, corresponding to the subject header in traditional mail systems. The text of the message is prompted with the phrase What is your request?, to which the user can enter any text whatsoever.

1The Coordinator is a workgroup productivity system created by Action Technologies, Inc., available for IBM PC-XT/ATTM-compatible machines. The description here focusses on the conversation manager, which is one part of an integrated system that also includes word processing, formatting, calendar maintenance and communication over modems and LANs. The Coordinator is a registered trademark of Action Technologies. The interface design is copyrighted, and aspects of it are reproduced here by permission. A patent is pending on the systems conversation manager.

```
|                           C O N V E R S E                          |
|                                                                    |
| OPEN CONVERSATION FOR ACTION          REVIEW / HANDLE              |
|    Request                              Read new mail              |
|    Offer                                Missing my response        |
|                                         Missing other's response   |
| OPEN CONVERSATION FOR POSSIBILITIES                                |
|    Declare an opening                   My promises/offers         |
|                                         My requests                |
| ANSWER                                  Commitments due: 24-Sep-84 |
|                                                                    |
| NOTES                                   Conversation records       |
```

> _Figure 2. Converse menu from The Coordinator (reprinted by permission from Action Technologies, 1987)._

The system makes no attempt to interpret this text, relying on the users understanding and cooperation that the message is properly identified as a request. This is a key design issue: Let people do the interpretation of natural language, and let the program deal with explicit declarations of structure (such as the users declaration that this is a request). This leaves users free to communicate in ordinary language that depends on the background of the reader. A perfectly understandable request might contain the single word Noon? if the participants have a shared understanding (e.g., they often go to lunch together).

When the user signals that the text is complete, the system prompts for three dates associated with the completion of the action: a respond-by date, a complete-by date, and an alert date. Date entries are optional, but experienced users almost always include one or more of them. Not only do they provide a structure for retrieval and for monitoring completion, but the use of specific dates plays a surprisingly large role in producing effective conversations. Although we will not emphasize this aspect in the present paper, the design of The Coordinator system grew out of Floress work in training people in communicative competence (Flores & Graves; 1968a, 1968b). In that work, Flores has demonstrated that peoples ability to communicate effectively (with or without support from computer systems) is improved when they develop facility in distinguishing the kinds of commitments people make in conversations for action, and the dimensions of time associated with the completion of those conversations.

When a user of the system receives a request (the details of message transmission and retrieval will not be discussed here), he or she has the option of responding by selecting Answer from a menu. This pops up a subsidiary menu as shown in Figure 3.

```
| SPEAKING IN A CONVERSATION FOR ACTION |
|                                       |
|  Acknowledge       Promise            |
|  Free-Form         Counter-offer      |
|  Commit-to-commit  Decline            |
|  Interim-report    Report-completion  |
```

> _Figure 3. Menu for responding to a request (reprinted by permission from Action Technologies, 1987)_

This menu is automatically generated by a conversational state interpreter from a network like that of Figure 1. The first three items in the right hand column (Promise, Counter-offer, and Decline) represent the actions available to the responder (B) in state 2. The fourth choice (Report-completion) is an action available in state 3, after B has promised. In some cases, it will turn out that B has already done what A requested, before having responded to initial request. In that case, the Promise act is implicit, and Report-completion is the next overt communication.

The left-hand column introduces conversation acts concerned with the conduct of the conversation itself, which do not advance its state. Acknowledge lets the requestor know that the request was received. Free-form allows any kind of communication relevant to the conversation that does not fit into the formal structure -- most frequently, notes, comments, and questions. Commit-to-commit would be conveyed in natural language with sentences like Ill let you know by Thursday if I can do it. That is, the speaker is committing to take the next conversational step (promising or declining) by a specific time.

When any answering action is selected, a new message is automatically generated with markers corresponding to the choice of act, and with a generic text. For example if the response is Promise, the initial message is I promise to do as you request. while for Counter-offer it is No; I counteroffer: The user can augment or replace this text using embedded word processing facilities. Experience has shown that a surprising number of messages need only the initial pro forma composition. The message initiating a request or offer needs to contain text that describes the action, such as Can you send me that report we were talking about?, but often the subsequent steps can be made by simply selecting the appropriate menu item and hitting the button that sends a message.

Whenever Answer is selected, the menu displays only those actions that could sensibly be taken next by the current speaker. State 2 of Figure 1 shows a Cancel action by A, in which the request is withdrawn. This will appear on As menu, but not on Bs. Or, for example, after making a promise in a conversation, then the next time B selects Answer in that conversation (assuming no intervening action by A), the menu offered will be as shown in Figure 4.

```
| SPEAKING IN A CONVERSATION FOR ACTION |
|                                       |
|  Free-Form       Cancel/New-Promise   |
|  Interim-report  Cancel               |
|                  Report-completion    |
```

> _Figure 4. Answer menu generated in continuing a promise (reprinted with permission from Action Technologies, 1987)._

At this point, B no longer has the option to decline (having already promised), but can Report-completion (moving to state 4) or Cancel (moving to state 7) with or without initiating a new promise.

The Coordinator has no magic to coerce people to come through with what they promise, but it provides a straightforward structure in which they can review the status of their commitments, alter those commitments they are no longer in condition to fulfill, make new commitments to take care of breakdowns and opportunities appearing in their conversations, and generally be clear (with themselves and others) about the state of their work.

#### 4.2. Retrieval and monitoring

The structure and status of conversations is the primary basis for organizing retrieval and review in the system. To put it simply, the structure is organized to provide straightforward and relevant answers to the implicit question What do I have to do now?.

In the main menu of Figure 2, under the heading REVIEW / HANDLE we find items such as Missing my response, Missing others response, My promises/offers, and My requests. When one of these is selected, the user is presented with a listing of conversations matching the selected item.

Several things are of note:

1) The basic unit of work in the system is a conversation, not a message. In conventional electronic mail systems, messages in a conversation are often linked by conventions such as the use of Re: ... in headers. For The Coordinator, each message (including a Free-form) belongs to a particular conversation. The retrieval structure is two-level, with the user first identifying a conversation, then selecting particular messages within it to be displayed.

2) The explicit use of conversation theory in the generation of messages makes it possible for retrieval to be based on status. There is a menu selection that selects and displays conversations in response to the question, In which conversations is someone waiting for me to do something? or In which conversations have I have promised to do things? Note that these are different. For example, if you make an offer to me, then our conversation is in a state where the next move characteristically belongs to me, but I have made no promise to you.

3) The distinction between open and closed conversations is used to filter out those to be retrieved. Unless the user designates otherwise, The Coordinator will display only those conversations that are still open to further action (not in one of the final states as shown by heavy circles in Figure 1).

4) Explicit completion and alert dates are used for time-oriented retrieval. The item Commitments due: ... on the menu allows retrieval of all conversations that need some action (either a response or a completion) on a date entered by the user. There is an additional menu that allows retrieval on precise combinations of dates, domains, and people involved in different conversational roles (e.g., the things Chauncey has promised to get done next week regarding programming). The calendar subsystem is integrated, so that all of these items can optionally appear at the appropriate places in a personal calendar, along with more conventional entries such as meetings and appointments.

The Coordinator is an example of basing a system on theories of language without attempting to program understanding. All of the interpretations (e.g., that a particular message is a request, or that it should be done by a certain time) are made by the people who use the system, guided by appropriate menus and prompts. This is not experienced by users as an extra job of annotating, but in fact replaces typing parts of the contents with more direct and structured interactions, which are often more efficient. It is a generic tool in the sense that a word processor is -- intended for a particular kind of communication, without regard to topic. A word processor is not equally well suited to generating all kinds of character sequences, but is specially designed for the words, sentences, paragraphs, and the like of ordinary written text. Similarly, The Coordinator system is not built for arbitrary sequences of messages, but for the requests, promises and completions that are at the heart of coordinated work.

### 5\. Conversations in a work setting

Conversations for action (CfA) form the central fabric of cooperative work. However, many kinds of language acts do not participate directly in the completion of a CfA. Remarks such as Theyre planning to remodel the West Wing next summer need not relate directly to any specific future actions of speaker or hearer. From a cognitive perspective, one might choose to characterize these as conveying information without a particular motivation in action. From the perspective of language as action, the primary concern is with the role that all conversations (and all utterances within conversations) play with respect to action and potentials for action. We distinguish several additional kinds of conversation that go along with conversations for action: conversation for clarification, conversation for possibilities, and conversation for orientation. There is no sharp line between them, but they are accompanied by different moods.

In a conversation for clarification the participants cope with or anticipate breakdowns concerning interpretations of the conditions of satisfaction for a CfA. The conditions are always interpreted with respect to an implicit shared background, but the sharing is partial and needs to be negotiated. As a simple example, the request Give the patient some diazine might evoke responses such as Right now, or with the morning meds? or What dosage?. One can never guarantee that everything is totally precise. Precision is relative to each partys implicit anticipation that the other party will have a sufficiently shared background to carry out the action in a satisfactory way.

In a conversation for possibilities, the mood is one of speculation, anticipating the subsequent generation of conversations for action. Specific conditions of satisfaction will emerge in the course of the conversation, and associated conversations for action will be initiated. Many gatherings that are called meetings are best conducted in this mood. The meeting is a failure if some action does not come out of the discussion. Some conversations for possibilities are highly routinized. For example, work rounds on a hospital ward is a routine conversation for possibilities, during which the medical team visits each patient and specific requests and commitments are generated.

In a conversation for orientation, the mood is one of creating a shared background as a basis for future interpretation of conversations. This shared background includes specific knowledge, interpersonal relations, and general attitudes. The most obvious examples are meetings labelled orientation, in which newcomers begin to develop the understanding that is required to function in the organization. Conversations for orientation are prominent in less formal settings (shooting the bull). Although the mood here is not directed towards action, it is important to recognize the importance of developing mutual orientation as the basis for future effective action and for appropriately shared interpretation of language acts.

Each of these types of conversation has its own regularities of structure, which in turn can be reflected in the design of the tools for conducting it. Just as the CfA structure of The Coordinator grew out of experience with conventional message systems, we can apply conversational analysis to the reinterpretation and redesign of other existing systems, such as help systems (which carry out a limited kind of conversation for clarification), group facilitation systems, such as Colab (Stefik et al., 1986) which are used in generating possibilities, and BBOARD and computer forum systems, which (among other things) facilitate conversations for orientation. We will not analyze these in detail, but will use the nursing example to show how conversations appear in the nursing setting, and to discuss some of the design considerations.

In the discussion we will comment on details of work on the hospital ward, as outlined in the Appendix. Although no computer applications were developed in that setting, one can imagine an integrated medication information system through which many of the activities would be replaced by actions on terminals (or workstations) at various sites, including the ward, the examining rooms, and the pharmacy. Records needed in places where direct computer access was infeasible could be printed out and posted. The information flow could be redesigned, eliminating redundancies and the need for manual copying or posting of information. It is far beyond the scope of this paper to develop a comprehensive design for such a system, but the setting can serve to illustrate our perspective.

#### 5.1. Conversations for action

In the hospital, there are many different conversations for action, with a variety of visible forms. Some are highly routinized, such as the primary CfA dealing with the administration of medications. Requests are made by doctors (either as standing cures or on the patient-carried paper scraps), to the treating nurse. Report of completion is represented on the curve sheet, and the declaration of completion is implicit in the doctors review of the records on his or her next visit. As a precondition for satisfying these requests, the nurse must receive the medicine, and there are CfAs (with the pharmacy) to get the medications, using prescription forms to make requests. In general, conditions of satisfaction are determined in a rigid way by the codes and blanks, perhaps with extra notations in natural language. Acceptance of an offer or request is assumed whenever it is not explicitly rejected. Completion is reported on a standard form, which, like all of the other forms, is associated with standards for interpretation, which are learned as part of the relevant professional training. In addition to these routinized CfAs there are unscheduled verbal conversations. For example, a request may be made by a doctor to a nurse at the bedside, with immediate explicit accept, decline, or counter-offer. Completion may be reported later via a note in the patients chart.

In a hospital, completion of conversations can be a life-or-death matter. There is a highly regularized structure of checks and crosschecks to ensure it, as illustrated in the Appendix. The regularization is both in the form of special activities (the various checklists) and the strict temporal routine. The fact that a particular action will be done at a particular time can be taken for granted on the basis of the daily schedule. The dependence on rigid forms and routines can be viewed an attempt to assure that conversations proceed smoothly in cases where personal contact is not sufficient. This could potentially be reduced, adding work flexibility, through the use of a conversation-based system in which the monitoring of completion (and coaching towards completing conversations) is incorporated in a communication medium.

There is also the potential to replace routine CfAs with declarations of recurrent responses. For example, rather than responding to each drug request, a pharmacist might establish an automated prescription filling system, which takes the data from the request and activates a mechanized dispensary. This is a common kind of computerization: computers take over those functions for which precise repetitive rules can be established. In designing these automated systems from a language/action perspective, we are led to consider the potential for secondary conversations. Who declares the distinctions that are embodied in the forms and rules? If the medication request does not match the standard form for designating medications, then who is involved in the conversation for clarification, and how? In conventional system design, there will always be de facto answers to such questions (especially after experience has pointed out the places for breakdown). Through a conversational analysis we can anticipate and de

#### 5.2. Conversations for clarification

Conversations for clarification are much less regular (as we would expect) and are often verbal. The crosschecking of the various forms also triggers these conversations when the different forms are not directly contradictory, but are open to conflicting interpretations. In designing tools for conversations for clarification, it is important to recognize their relative lack of recurrence. Recurrent differences of interpretation will lead to the declaration of new distinctions or new forms for making requests and commitments that are clear. But there will always be irregular, unexpected cases, and computer-based systems that provide only rigid forms may make it difficult or impossible to deal with them.

#### 5.3. Conversations for possibilities

Much of what appears to be useless copying or verification of redundant information on the hospital ward is really a routine way of generating conversations for possibilities. For example, in the review of medications (see Appendix):

Only a minor part of the 30 minutes was used for updating and comparing. The rest of the time was spent on small conversations, initiated by findings in the information they were handling. Some examples of what the nurses did: Reporting to each other about the patients state and activities; deciding what were facts when inconsistencies were found; deciding changes in some medicines after small negotiations; reminding the treating nurse of a test that had been forgotten; investigating why a medicine was not delivered from the chemists; finding out why a patient had to take a specific test.

If the medication review were replaced by an automated process, the opportunity for this kind of conversation could be lost. It could be reinstituted in other ways if it were recognized in the analysis. Similarly, if the curve sheet is replaced with a table of drugs, dosages and times, it is no longer possible for the nurses to use it as a vehicle of communication (in the notes) for the small conversations dealing with specific breakdowns and subsidiary CfAs. It might well be possible to replace it with a better vehicle for these conversations, once their importance is recognized.

#### 5.4. Conversations for orientation

When asked to comment on the systems analysis, the nurses felt that it did not capture the aspect of their activities that dealt with the total picture rather than with the specifics of particular medications and tests. The existing structure provides explicit routines to allow for open-ended conversation, such as the morning report, where One nurse is informing the other staff of the status, changes and performed activities of each patient during the last day and night. Informal exchanges among the nurses include both explicit CfAs and more general orienting discussion about the total picture. One form of orienting conversation is the telling of stories, whether in the direct line of work, or around the coffeepot. Orr (1986) describes the importance of relating war stories as part of technical training. One has only to spend a short time in the company of medical workers to realize how prevalent this activity is. Computer BBOARD systems sometimes play this role within the community of computer researche

#### 5.5. The larger web of conversations

Finally, the conversational analysis includes not only those immediately visible, but also the larger web of conversations in which they are situated (Kling & Scacchi, 1982). One obvious example in the hospital is the legal conversation about the quality of care. All written records are potential evidence in a malpractice suit, and the people who create and manipulate them are aware of this possibility. In addition to the legal conversation, there are ongoing conversations about the hiring, evaluation, and dismissal of employees. Kaasbll notes (1986, p. 11): If the nurses make mistakes, they may be sued by the patients, and they may be punished by the hospital administration. This gives an incentive for not recording mistakes in the Kardex.

Certain conversations will inevitably go on outside of any written (or electronically stored) system. Explicit records will never correspond to an objective reality, but are the result of declarations by individuals, with their own interpretations and purposes. No computer system can change these fundamental facts about how humans function in organizations, but an explicit understanding of the larger network of conversations can help to recognize the roles that language acts play in a variety of conversations, and to match expectations to those roles.

### 6\. Semantics

The previous sections have introduced conversation types in a very general sense, without considering what the conversations are about. Of course there is also a high degree of recurrence in content, which is apparent in the amount of organizational communication conducted with forms of various kinds (including electronic forms). When a doctor requests medication for a patient, we can identify the generic action as a Request in terms of the CfA structure given above, and we could use a system like The Coordinator to monitor its completion. From a slightly different angle, we can see it as an instance of a Medication Order conversation, which is specified by filling in standard blanks, such as the patients name, the identity and quantity of the drug, etc. The doctor could take a single action (e.g., a menu selection) to bring up a display with the relevant items indicated, and with some of them initially filled in (e.g., the date). Others might be filled automatically (for example, the standard dosage when t

None of this is new. Business programs along these lines can be found in every walk of life from the airline counter to the grocery store. We can think of these systems as embodying frozen conversation structures. In designing the forms and interactions, programmers embody their understanding of a specialized conversation structure and a set of procedures for completing the conversations. General facilities for specifying office information systems are described by Ellis and Nutt (1980), and in the more recent research exemplified by Malone et al. (in press). A flexible specification formalism for forms (or messages) and relationships among their parts makes it easier to design appropriate forms and blanks, and to support automation.

From a language/action perspective, two fundamental issues appear. First, there is the role of conversation structure. The Medication Order form encodes an action (a request) in a particular conversation. Another form, such as the Nurses patient report may embody a further action in the conversation (e.g., reporting completion). These linkages can be the basis for retrieval and presentation, as well as providing structure for the overall system and the procedures that go with it.

Second, semantics is subordinate to language action. Traditionally, semantics has been described as a correspondence between the forms of a language and some kind of truth conditions on the world of which it speaks. The analysis concentrates on deriving meaning from the systematic combination of elements. One takes for granted a collection of basic terms -- the nouns, verbs, adjectives and the like -- referring to identifiable objects, properties, relations, and events in the world. From the perspective of language as action, words cannot be defined in isolation from a particular conversational setting in which they are used. The distinctions that are reflected by the choices among words arise through recurrent patterns of conversation, in which breakdowns of action lead to new distinctions (Winograd, 1985; Winograd & Flores, 1986).

This is equally true in our extended linguistic perspective. A computer-based form has a syntax in which the individuals fields and their fillers are the basic units. The interpretation of a field marked Status cannot be based on a general definition of what a status is. It will depend on the context and background of the people who enter, interpret, and use the records. The communication will be effective only to the extent that relevant background is shared. Texts on business data processing discuss the importance of data dictionaries, which prescribe the meanings of the individual records and fields in a data base. Behind that activity there are questions as to where definitions come from, how they are represented, and how they are understood by the people who use them. These are analogous to problems in natural language.

#### 6.1. What domains of distinctions are taken as background?

Everyone in a normal work setting shares a natural language and a lifetime of cultural experience. The everyday use of language takes this for granted, using ordinary vocabulary along with common technical terminology, such as that of the clock and calendar. Other meanings will be specialized to a professional area such as medicine. The boundary between natural and specialized domains is not sharp -- many words are used in both informal and semi-formalized, or stylized ways. The patient is in stable condition has a technical interpretation distinct from the natural one. In some cases, such distinctions may be set down by formal rules; in others, learned through practice.

A crucial part of professional training is learning a jargon -- the distinctions and associated terms that provide a basis for inventing and taking relevant actions. Profession-oriented languages (Kaasbll, 1986) are an attempt to integrate this specialized language structure into the design of computer-based systems. Kaasbll (in press) points out problems, such as locally-used distinctions that are not standard to the field and not immediately available to system designers. For example, the nurses in his study referred to a lung-function test apparatus as the Ohio, which was its brand name, and they had no more general term. In some cases such matters are of critical importance to conditions of satisfaction. In the medical profession two different kinds of terms are used to describe medications: brand names (Tylenol) and generic names (Acetiminophen). A request made for a brand name may or may not be satisfied by an equivalent generic, depending on a complex interaction of standard practices and local regula

Suchman (1987) describes the problems that arise from failing to account for differences in semantic interpretations when designing user interfaces. In a user-friendly interface for a copier, language about the machine and the users actions appeared in various forms on the screen, using distinctions and words that made perfect sense to the copier-designers, but that led to serious breakdowns for users without the same background. In one case, failure to distinguish the document cover from the bound document aid led to interpreting help instructions in a way completely different from what the designers intended.

The point here is that the system designer cannot assume that the semantics -- the mapping from words to distinctions of interest -- will either be natural or follow some existing formal specification of the domain. This is especially relevant in a setting like the hospital, where conflicting languages are already in use (the language of doctors, nurses, ordinary language, etc.).

Along with the specific conversations and forms, the system designer participates in designing the professional language of the workplace. A new computer system will alter the language, both in interactions with the system, and in the work around it. Andersen and Madsen (1986) point out the change in usage of the word document when an indexing system was designed for a document collection, then extended to the whole library. All of the indexed items (including books, magazines, etc.) came to be called documents, contrary to prior usage. There is both a danger of creating confusion and an opportunity to shape the conversations and the work itself.

#### 6.2. How do new distinctions emerge?

New distinctions are always emerging because of new breakdowns or anticipation of them. A frequent reason for the failure of computer systems is that they lock in a set of distinctions without provision for evolution. Gradually people find more and more need to work around the system, leading to complexity and chaos.

For example, based on the manual forms used by the dieticians, a patients diet might be recorded as one of a fixed set of choices, such as no salt, diabetic, etc. Imagine that a new kind of diet is added, such as limiting the cholesterol within the existing diets. The new distinction is not simply one more alternative but modifies each of the pre-existing choices. We might add a collection of new diets such as no salt low cholesterol, diabetic low cholesterol, etc. but this is a work-around. If a further qualification (high potassium) is added, the system will begin to bog down. What is needed is an interpretation of diet as combining a set of separable dimensions, instead of as a simple choice. The original system designer could not anticipate this need. Gerson and Star (1986) describe the problems that arise and the need for what they call due process in maintaining shared understanding. Kaasbll (1986, p. 10) gives an example of a technical term whose meaning was subject to argument and the imposition of authority:

During a doctors visit, the doctor and two nurses started a conversation of what P1 means. P-values are measures of obstructions in the lungs.

> Doctor: It is the air in the lungs that counts, not the sounds.
> 
> Nurse1: It is obvious that Peter (the chief physician) has a different opinion of P1 than you.
> 
> Nurse2: One has to remember that there are individual discrepancies between the children, such that P1 does not mean the same for one child as for another.

This discussion can be interpreted as a negotiation over the semantics of P1, and thus as a development of the language at the ward. It can also be seen as part of the power struggle between the two professions involved.

The larger pragmatic analysis of conversations and roles includes the conversations in which meaning is negotiated, and their reflection in a computer system.

#### 6.3. How are distinctions indicated?

Much of the traditional work on natural language semantics adopts the idealization of a relatively straightforward compositional mapping from forms to meanings. Put simply, each basic term (word) has a meaning, and each phrase or sentence has a meaning made up from the meaning of its parts in a standard way. Some current research goes further, focussing on the effect of context on meaning. It is based on structured analyses of contexts (both the linguistic context and the situation of the speaker and hearer) and the relation between those structures and the meanings of utterances. There has been some interest in applying the resulting theoretical framework to non-natural languages, such as programming languages and human-computer interfaces (CSLI, 1984). It is beyond the scope of this paper to survey the relevant work. It has significant limitations, as discussed by Winograd (1985).

As an example, consider the meaning of filling in a medicine card listing a patients medications. From a standard semantic view, each blank would be filled with a term that denoted a particular medication, and the card as a whole (analogous to a sentence) would enumerate all the medications to be given to the patient. This is typically the case, but according to Kaasboll (in press, p. 4):

The sheets were filled in properly during the 30 minutes, except for a couple of observed missing medicines on the medicine cards. When asked about the mistakes the treating nurse replied: Oh, but we know he (the patient) is going to have the medicines even if it is not written here. It is erased only because he has been under intensive care for some days.

The issue here is not the exact form of the cards. It could just as well have been a computer system with database entries for medications. The situation-dependence of meaning is in the people who enter and access the data. Accuracy is not just a matter of having the computer keep its records straight. In designing and using a system, it is critical to understand the different potentials for interpretation and either cope with them or modify them through training.

The point of all this from the language/action perspective is to treat the generation and interpretation of semantic distinctions as an activity based on conversations that can be designed and facilitated through the computer. One general principle pointed out by Nygaard (1986) is the importance of having distinctions that are open to new interpretation by the workers. In practical terms, this may be as simple as having a Notes field in some data record, that allows the worker to enter (and retrieve) ordinary natural language text, as opposed to fixed fields, in which the distinctions are fixed by system convention. It may also lead to new kinds of structured conversations within the work.

### 7\. Blindnesses of the language/action perspective

Technological impacts cannot be fully understood from any one perspective. Each perspective brings forth some concerns and is blind to others. In designing a coherent system we are guided by a choice of perspective, but success comes from anticipating breakdowns that only become visible from other perspectives. A number of other perspectives will interact with a design generated from concerns of language action:

#### Implementation

From an implementation perspective we are concerned with issues of hardware, operating systems, languages, data formats, and the like. The vast bulk of the detailed literature on system design approaches problems from this perspective, as it must for practical reasons.

#### Web of computing

As Kling and Scacchi (1982) point out, we cannot look at the computer system in isolation. The implementation design is part of a larger web of issues surrounding the computer system itself, such as the design, acquisition, installation, maintenance, and hiring and/or training of people to use a system. These include economic, political, and social considerations and each of these has its own domains of conversation, possibilities and breakdown. In a way, this perspective is at the opposite end from implementaton---these are the concerns that ultimately must dominate practical choices, but they do not provide a structured basis for creating a design.

#### Information processing

Traditional system perspectives have centered on the kinds of information being entered, stored and accessed, and on the logical rules relating them. As with implementation, this is obviously the perspective from which many details have to be approached. Our relative lack of attention to those issues here does not mean that they are unimportant. Our argument is that, like implementation, they should be looked at in a subordinate way, guided by considerations of the role they play in the structure of language actions by the people using the system.

#### Roles, locations, and materials

Holt, Ramsey, and Grimes (1983) present a role/activity theory that focusses on peoples roles (which specify sets of behaviors) and on the temporal and spatial structure of their potential interactions. Holt (1986) notes that What first stands out in any work environment is its architecture---that is to say its spatial-functional organization.... Functional proximity is what relates work places to each other. It is the relation which constrains and organizes the movement of people and materials...

From a language/action perspective we can understand roles in terms of potentials for entering into particular recurrent conversations. But we do not have any tools for describing the distribution of materials or the physical potential for interaction. There may be a critical difference between putting a single terminal at the main nursing station, putting a terminal in each examining and activity room, and having one available by every bedside. In looking at the role of an individual, we need to recognize that his or her body can only be in one place at one time, and is limited in its ability to move from place to place. In a way this sounds mundane, but it is all too easy to design a system that would work wonderfully---if the nurse would walk over to the nursing station before giving each patient medication---but which doesnt succeed in practice.

#### Authority

An important aspect of every human organization is the distribution of authority and the mechanisms by which it is maintained. The introduction of a new technology can perturb this structure in a variety of ways: facilitating detailed monitoring of performance; making it possible for subordinates to work in ways that are not understood by their superiors; and opening possibilities for communication that crosses lines of authority. An analysis of conversational roles can identify particular individuals as having the ability to initiate or respond in certain conversations, and this structure is the practical consequence of authority. But the mechanisms by which authority is established and maintained go beyond this. In contrasting the tool perspective to a more traditional systems perspective, Ehn and Kyng (1984) focus on this issue, looking at ways to maintain the autonomy of workers in the face of computer-based changes that can potentially be used to expand centralized authority.

#### Group interests

Work is not carried out by a homogeneous collection of individuals. Every work setting contains groups with collective interests, which can be affected by the introduction of computer systems. The redesign of work is a negotiation among the groups already doing and supervising the work, and the results will be shaped by the interests of these groups and the compromises among them. This kind of issue is often critical to system design, for example between journalists and typographers in newspaper-publishing systems (Howard, 1985) and between librarians and clerks in libraries (Andersen and Madsen, 1986). In the hospital, there are powerful constraints on the appropriate role behavior of doctors and nurses. The structure of interactions within the organization maintains this identity and changes can threaten it. In our example, one might imagine merging the various records and thus eliminating the Kardex. But, according to Kaasboll (in press):

Nurses are traditionally a paraprofession subordinate to the physicians and their medical knowledge.... In the nurses struggle for acceptance of nursing as a profession, the theoretical concept nursing process and its practical documentation in the Kardex is of central importance for developing nursing as a science on its own. In this struggle, the Kardex as a basis for nursing decisions may be seen as the nurses answer to the physicians medical records.

#### Conflict

Most of the organizational models applied to information system design are based on the assumption of shared goals among the participants. In real organizations there are always conflicts among competing goals held by different individuals and groups. In some cases this is institutionalized (as in contractual labor-management relations or internal market competition in a firm), but it is always present. A system that assumes idealized cooperation may easily fail as the result of behavior that the systems analyst might label as stupidity, sabotage, or just plain human stubbornness. An analysis that takes conflicting interests into account is not a vain attempt to dissolve them, but can channel them into explicit forms of mutually agreed-upon negotiation. The language/action perspective establishes a structure for negotiation, based on a theory of cooperation that assumes the willingness to enter into serious conversation, without assuming shared goals or agreement. A conversation for clarification, for example, might involve each party's negotiating to get a favorable deal, but it can nevertheless result in a mutual agreement. More work needs to be done in integrating a conflict perspective (Ciborra, 1985; Nygaard, 1986).

#### Interpersonal relations

One of the most obvious effects of computer systems is the replacement of face-to-face verbal interaction with computer-mediated exchange. Some of the potential problems can be characterized in conversational terms. A face-to-face interaction that is identified as playing a particular role in conversations for action (e.g., medication record entry) often has other components (conversations for possibilities) that are lost when it is replaced with computer interactions. Language acts, in general, can be less effective in the absence of personal relationships. In a study of the introduction of a production planning and control system into a factory, Schneider and Howard (1985, pp. 14--15) noted:

In the contributing areas, Production Support personnel are constantly engaged in informal discussions, promises, and agreements.... Schedulers spend nearly half their time in meetings, competing with their colleagues over shop capacity and priority (one likens the process to butting heads). Thus, a major part of the production planning and control process involves the extremely social acts of persuasion, negotiation, and, at times, argument. As one Production Control expeditor puts it, Im just one leaf on the tree. I try to go in any and all directions in order to get a part out. It all depends on developing working relationships with people in other departments---purchasing, quality control, manufacturing engineering. Its a matter of trust built up over time. Personalities play a big role in it.

In their study, they show the pitfalls of trying to redesign the work to eliminate these interactions. Although the language/action perspective focusses on the conversations among individuals, it is structural, not psychological. It asks us to look at the potentials for interaction, but not the motivations and feelings that will lead to what people actually do. Questions of mood, motivation, and personal satisfaction go far beyond anything that has been dealt with here, and are essential to successful design.

### 8\. Conclusion

We began with the declaration that a system designer benefits from having an explicit awareness of perspective. A perspective generates concerns and questions, and provides a structured analysis through which they can be addressed. Although every design must eventually confront issues from all perspectives, its overall direction is strongly affected by the ones taken as primary. We have shown how cooperative work can be interpreted as the generation of language acts and conversations. Experience with The Coordinator has demonstrated the value of this perspective in designing workgroup communication tools. In its capacity as a general medium for conversations for action, it has improved work capacity and effectiveness in a variety of settings. The next step will be to apply the language/action perspective to the design of systems that deal with the recurrent content of conversations, with the other types of conversations, and with the relations linking one conversation to another.

There is little agreement as to what core issues will define the area of research in office systems and computer-supported cooperative work. The fields cannot be defined by particular implementation techniques, or principles of information processing, since these apply to all computer systems. We believe that they are part of a new discipline that focuses on the interaction between the structure of systems and the structure of work, and we anticipate that the language/action perspective will play a major role in its development.

### Acknowledgments

My conversations with Fernando Flores have been the basis for my understanding, in the most fundamental ways. Without his teaching, my perspectives would have been far different. I wish to thank the participants in the working meetings on system development at the Center for the Study of Language and Information at Stanford for their valuable contributions to the evolution of this work. Jens Kaasbll and Kim Halskov Madsen were especially helpful in giving me access to and a better understanding of the work being done in the SYDPOL projects. Chauncey Bell, Bradley Hartfield, Franoise Herrmann, Mary Holstege, Judy Olson, and Liam Peyton gave insightful critiques of earlier drafts.

### Appendix: Activities on a hospital ward

(adapted from Kaasboll, 1986, p. 3)

In a case study described by Kaasbll (1986), researchers in the Florence project of the Scandinavian research program on System Development and Profession Oriented Languages (SYDPOL) analyzed work on a ward of a Norwegian hospital, from what they call a systems perspective. They focused on the tasks associated with giving medications in a ward for children with respiratory problems. The Appendix paraphrases Kaasblls verbal description of some of the activities that were analyzed.

Each nurse has a special responsibility as the team nurse for a small group of patients.

On the day shift, one nurse (called the treating nurse) has the task of giving medicines. Her working day may be characterized roughly by the sequence: attend the report meeting; give medicines; record the medicines given; take care of children in kindergarten or the dining hall.

The report meeting takes place from 7:45 to 8 am. One nurse informs the other staff of the status, changes and activities of each patient during the previous day and night. She has heard a vocal report from the night shift, and she reads the Kardex while reporting. The Kardex contains diagnosis, planning and evaluation for each patient, and a form with fixed main patient information. It is supposed to be up to date. Other staff take notes on their program sheets.

Medicines are prescribed by the doctors on prescription forms in cures lasting several days or in daily doses. Cures are recorded on the main patient information form and on the medicine card.

Medicines are given in a treatment room between 8 and 9:30 am. Patients enter after having been examined by a doctor, carrying with them a scrap of paper on which the doctor has written todays dose and possible changes in cures. Prescriptions for medicines during the intervals between the regular medicine hours are noted down on a premedlist hanging on the wall in the treatment room.

Some simple lung function tests are also performed in the treatment room to monitor the effects of the medicines. Tests to be taken are written on the prescription form and on a scrap taped to the medicine card or on the program sheet if there are changes. The test results are recorded on special forms.

After having given medicines, the treating nurse brings her papers to the ward office. Together with each of the team nurses, one at a time, she examines the papers. All medicines given are now registered on the curve sheet. Changes in cures are recorded in the Kardex, and on the medicine card and eventually on the premedlist. In addition, all sheets are compared for the sake of control. The patients are processed one by one. The team nurse reads from her papers which medicines are to be given. The treating nurse answers by stating which are actually given, and the state of the patient. One day, when the load on the nurses was relatively low, this activity lasted from 9:30 am to 13:25 pm. During these 4 hours, at most 30 minutes were effective paper work. The rest was delays, either because some of the papers were used by others, or because one of the nurses was engaged in handling interruptions. Only a minor part of the 30 minutes was used for updating and comparing. The rest of the time was spent on small conversations, initiated by findings in the information they were handling. These included:

#### References

Action Technologies, Inc., (1987) The Coordinator Workgroup Productivity System I. Version 1.5P. Emeryville, California.

Andersen, P. B., & Madsen, K. H. (1986). How to handle the intangible: Metaphors in design and use of computer system, Technical report, Aarhus University.

Austin, J. (1962). _How to Do Things with Words_. Cambridge, Massachusetts: Harvard University Press.

Ciborra, C. U. (1985). Reframing the role of computers in organizations, the transaction costs approach, Sixth Annual International Conference on Information Systems, Indianapolis.

Center for the Study of Language and Information (1984). Research Program on Situated Language, Report CSLI-1, Stanford University.

Ehn, P., & Kyng, M. (1984). A tool perspective on the design of interactive computer support for skilled workers. In M. Saaksjarvi (Ed.), _Report of the Seventh Scandinavian Research Seminar on Systemeering,_ Helsinki.

Ellis, C. A., & Nutt, G. J. (1980). Office information systems and computer science. _Computing Surveys_ 12, 27-60.

Flores, C. F. (1981). Management and communication in the office of the future. Unpublished doctoral dissertation, University of California at Berkeley.

Flores, C. F. & Graves, M. (1986a). Domains of permanent human concerns. Unpublished report, Logonet Inc., Berkeley.

Flores, C. F. & Graves, M. (1986b). Designing education. Unpublished report, Logonet Inc., Berkeley.

Flores, C. F., & Ludlow, J. (1981). Doing and speaking in the office. In G. Fick & R. Sprague (Eds.), _DSS: Issues and Challenges._ London: Pergamon Press, 1981.

Gerson, E. M., & Star, S.L. (1986). Analyzing due process in the workplace. ACM Transactions on Office Information Systems 4, 257-270.

Haugeland, J. (1981). The nature and plausibility of cognitivism. In J. Haugeland (Ed.), _Mind Design_. Cambridge, Massachusetts: Bradford/MIT Press, 1981.

Holt, A. (1986). Primitive man in the electronic work environment. Conference on electronic work, Milan.

Holt, A., Ramsey, H.R., & Grimes, J.D. (1983). Coordination system technology as the basis for a programming environment. _Electrical Communication_ 57 307-314.

Howard, R. (1985). UTOPIA: Where workers craft new technology. _Technology Review_ 88, 43--49.

Kaasboll, J. (1986). Intentional development of professional language through computerization: A case study and some theoretical considerations. _Proceedings of the IFIP Working Conference on System Design for Human Development and Productivity through Participation_ Amsterdam: North Holland.

Kaasboll, J. (in press). Observation of people working with information: A case study. Submitted for publication

Kling, R. (1980). Social analyses of computing: Theoretical perspectives in recent empirical research. _Computing Surveys_ 12, 61-100.

Kling, R., & Scacchi, W. (1982). The web of computing: Computing technology as social organization. In M. Yovits (Ed.), _Advances in Computers, Vol. 21,_ 1-90.

Malone, T.W. (1985). Designing organizational interfaces. _Proceedings of the CHI 85 Conference on Human Factors in Computer Systems_, 66-71. New York: ACM.

Malone, T.W., Grant, K.R., Turbak, F., Brobst, S.A., & Cohen, M.D. (in press). Intelligent information sharing systems, Communications of the ACM.

Malone, T.W., Grant, K.R., Lai, K.Y., Rao, R., & Rosenblitt, D.A. (in press). Semi-structured messages are surprisingly useful for computer-supported coordination, ACM Transactions on Office Information Systems.

Nygaard, K. (1986). Program development as a social activity. In H-J. Kugler (Ed.) Information Processing 86, 189-198. New York: Elsevier (North-Holland) .

Nygaard, K., & Sorgaard, P. (1985), The perspective concept in informatics. Precedings of the _Aarhus 1985 Working Conference on Development and Use of Systems and Tools._ Aarhus University, 1985.

Orr, J. (1986). Narratives at work, story telling as cooperative diagnostic activity. _Proceedings of the Conference on Computer-Supported Cooperative Work_, 62-72. Austin, Texas: MCC.

Schneider, L., & Howard, R. (1985). Office automation in a manufacturing setting. Unpublished study prepared for the United States Office of Technology Assessment.

Searle, J. R. (1969). _Speech Acts_. Cambridge: Cambridge University Press.

Searle, J. R. (1975). A taxonomy of illocutionary acts. In K. Gunderson (Ed.), _Language, Mind and Knowledge_, 344-369. Minneapolis: University of Minnesota Press.

Stefik, M., Foster, G., Bobrow, D.G., Kahn, K., Lanning, S. & Suchman, L. (1987). Beyond the Chalkboard: Computer support for collaboration and problem solving in meetings. _Communications of the ACM_, 30, 32-47.

Suchman, L. (1987). _Plans and Situated Actions: The Problem of Human-machine Communication_. Cambridge: Cambridge University Press.

Winograd, T. (1985). Moving the semantic fulcrum. _Linguistics and Philosophy_, 8, 91-104.

Winograd, T., & Flores, F. (1986). _Understanding Computers and Cognition: A New Foundation for Design_. Norwood, New Jersey: Ablex.
