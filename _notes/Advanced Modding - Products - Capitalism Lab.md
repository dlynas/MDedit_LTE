---
source: www.capitalismlab.com
url: https://www.capitalismlab.com/mod/advanced-modding/advanced-modding-products/
---

You may modify products in Capitalism Lab by editing the following DBF files.

### **Product\_Mega\_Classes.DBF**

This file defines mega product classes.

For more details about mega product class, see this web page: [Mega Product Class](https://www.capitalismlab.com/improvements/mega-product-class/)

| **Field** | Type | Length / Range | Description |
| --- | --- | --- | --- |
| MEGACLAS | Character | 8 chars | The code of the mega product class. |
| NAME | Character | 30 chars | The name of the product mega class. |

### **Product\_Classes.DBF**

This file defines product classes.

The relationships: Product Mega Class -> Product Class -> Product Type

When you add a new product class, you must also update Retail\_Store\_Products.DBF by specifying which types fo retail stores are able to sell products of the new product class. If you forgot to do so, when you attempt to add new products from the new product class to a retail store, you will find that Pick Supplier window will never show them.

### **Product\_Classes.DBF**

This file defines product classes.

The relationships: Product Mega Class -> Product Class -> Product Type

When you add a new product class, you must also update Retail\_Store\_Products.DBF by specifying which types fo retail stores are able to sell products of the new product class. If you forgot to do so, when you attempt to add new products from the new product class to a retail store, you will find that Pick Supplier window will never show them.

| **Field** | Type | Length / Range | Description |
| --- | --- | --- | --- |
| CLASS | Character | 8 chars | The code of the product class. |
| NAME | Character | 30 chars | The name of the product class. |
| LOCALCOMP | Numeric | 0 to 100 | It defines how competitive local companies are at this product type. A higher value means greater competitiveness. |
| MEGACLASS | Character | 8 chars | The code of the mega product class. |
| FARMRELATE | Numeric | 0 to 100 | This variable indicates the extent to which this product class is related to farming.
It is used for aiding the AI in making decisions.

E.g. The value for Livestock products is 100 as livestock products such as Eggs are produced in farms.

The value for Beverage products is 60, as beverage products do not depend entirely on farming for improving their product quality.

 |
| EXPERTISE | Character | ‘Y’ – Yes

OR

‘N’ – No

 | Whether a person may have expertise in this product class.

If this is set to ‘N’ (No), no one will ever have expertise in this product class.

 |

---

### **Product\_Types.DBF**

This file defines product types.

The relationships: Product Mega Class -> Product Class -> Product Type

| **Field** | Type | Length / Range | Description |
| --- | --- | --- | --- |
| CLASS | Character | 8 chars | The code of the product class. |
| CODE | Character | 8 chars | The item code of the product. |
| NAME | Character | 21 chars | The product name. |
| PRICE | Numeric | 0.3 to 20000 | The standard price of the product.
When a company is selling a product of this type at a higher price than the standard price, the product’s price rating (which contributes the product’s overall rating in the game) will drop.

Conversely, when a company is selling a product of this type at a lower price than the standard price, the product’s price rating will increase.

In addition, this is also affected by the wage level and inflation in the game. Products being sold in a city with a lower wage level will have lower standard prices.

 |
| RD\_PREMIUM | Numeric | 0 to 1000 | This is the component of the product price that is NOT affected by inflation nor wage rates.

For example, Smart Phone’s PRICE is 600 and RD\_PREMIUM is 200. Its standard selling price would be 600+200 = 800. The core component of the total price (600) will go up over time with inflation and is also affected by the wage rate of the city where the product is being sold. On the other, the R&D Premium price component (200) is not affected by inflation nor wage rates.

This setting explains why prices of smart phones are partially decoupled from inflation as they require constant investment in R&D. The technological leaps add tremendous values to the products while keeping the production costs in check.

 |
| FREIGHT | Numeric | 1 to 100 | The freight cost index. A large value means that the freight cost for shipping the product is high relative to the product’s selling price.

E.g. for two products whose selling prices are both $100. The one with a freight cost index will have a higher freight cost than the other for shipping the same quantity of products.

 |
| UNIT | Character | 6 chars | The measurement unit name of the product. |
| UNITS | Character | 6 chars | The measurement unit name of the product in plural.

(Leave it empty if it is the same as the measurement unit name for a single product.)

 |
| DEMAND | Numeric | 0.001 to 999 | It is the annual demand from a single consumer for the product on average.

E.g. a value of 10 means that on average a consumer will buy 10 units of the product annually.

 |
| NECESSITY | Numeric | 0 to 10 | The necessity index of the product. Enter a value from 0 to 10 here and it will automatically be multiplied by 10 to become 0 to 100 in the game. |
| PRICE\_CN | Numeric | 0 to 100 | The price concern of the product. |
| QUALITY\_CN | Numeric | 0 to 100 | The quality concern of the product. |
| BRAND\_CN | Numeric | 0 to 100 | The brand concern of the product. |
| CANINV\_YR | Numeric | 0 OR

1990 to 2999

 | This is defined for a product that needs to be invented via R&D. This variable indicates the year in which the product will become available for research and development in R&D centers. |
| INVENT\_YR | Numeric | 0 to 999 | This is defined for a product that needs to be invented via R&D.

This variable indicates the number of years that it takes to invent the product.

The actual R&D duration in the game will be shorter for R&D units of higher levels and for R&D units linked as a group for conducting R&D.

 |
| TECH\_IMPT | Numeric | 0 to 9 | This variable, which indicates the technology importance for semi products, is used by AI companies in the game only.

Since a semi product does not have the attribute “Quality Concern” as in consumer products, when AI companies consider whether it is worth investing into R&D for improving the quality of the semi product, this “Tech Importance” variable will aid the AI to make decisions.

 |
| IMPORT | Character | empty or ‘N’ | If it is set to ‘N’, it means that the product will never be imported via seaports. |
| PARENT1 | Character | 8 chars | If the product needs to be invented via R&D, you may define pre-requisite products for the research.

You may define up to 2 pre-requisite products (PARENT1 and PARENT2) and the product will only become available for research in R&D centers when all the pre-requisite products have already been invented.

 |
| PARENT2 | Character | 8 chars | The item code of the second pre-requisite product. (optional)

See above for details.

 |
| OUTBY | Character | 8 chars | If this is defined, the current product will be phased out by the product defined by this variable. (The variable name “OUTBY” means “phased out by”)

See more details about products phasing out products, see this web page: https://www.capitalismlab.com/new-content/enhanced-product-simulation/

[Click here for examples](https://www.capitalismlab.com/mod/advanced-modding/advanced-modding-phasing-products/)

 |
| OUTSPEED | Numeric | 0 to 100 | Only define this variable if the current product will be phased out by another product.

It indicates the speed at which the product is phased out by a new product, as defined in the variable OUTBY.

[Click here for examples](https://www.capitalismlab.com/mod/advanced-modding/advanced-modding-phasing-products/)

 |
| OUTREMAIN | Numeric | 0 to 100 | Only define this variable if the current product will be phased out by another product.

It indicates the remaining consumer demand for the current product after the phasing out process has completely occurred.

E.g. the introduction of Tablet Computers will draw sales from Notebook Computers. When you define this variable for Notebook Computers as 40, it means that Notebook Computers will still keep 40% of its original consumer demand intact, while 60% of the demand will eventually go to Tablet Computers.

[Click here for examples](https://www.capitalismlab.com/mod/advanced-modding/advanced-modding-phasing-products/)

 |
| OBSOLETE | Numeric | 0 to 100 | This variable is defined for products whose demands will drop annually on a continuous basis.

E.g. Cigarettes’ demand will be decreased by 2% each year, as this variable is set to 2 for cigarettes.

No external factors are required to trigger the decline in demand – it will just happen.

 |

---

### Retail\_Store\_Products.DBF

This file defines the types of products that can be sold in each type of retail stores.

| **Field** | Type | Length / Range | Description |
| --- | --- | --- | --- |
| BUILDCODE | Character | 8 chars | The building code. |
| ITEMCODE | Character | 8 chars | The product code. |

**NOTE:**

For numeric variables, if you enter a value that is outside the Range listed above, the game will automatically correct it when it loads the DBF files.
