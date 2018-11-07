
from flask import Flask
from flask_pymongo import PyMongo

import pprint

  mongo.db.items.insert_many([{
      "Image": ['1.1.jpg', '1.2.jpg', '1.3.jpg', '1.4.jpg'],
      "Brand": "Highlander",
      "Short Description": "Slim Casual Shirt",
      "Description": "White Slim Fit Casual Shirt",
      "Mrp": 999,
      "Discount": 45,
      "Price": 549,
      "Size": {'38': 0, '40': 25, '42': 10, '44': 6},
      "Product Details": "White casual shirt, has a spread collar, a full button placket, a patch pocket, long sleeves with roll-up button tabs, a curved hemline",
      "Material & Care": ['100% cotton', 'Machine-wash warm']
  },
      {
      "Image": ['2.1.jpg', '2.2.jpg', '2.3.jpg', '2.4.jpg'],
      "Brand": "Campus Sutra",
      "Short Description": "Men Regular Fit Casual Shirt",
      "Description": "Campus Sutra Men Blue Standard Regular Fit Self Design Casual Shirt",
      "Mrp": 1399,
      "Discount": 65,
      "Price": 489,
      "Size": {'38': 0, '40': 25, '42': 10, '44': 6},
      "Product Details": "Blue self-design casual shirt, has a cutaway collar, button placket, 1 pocket, long sleeves, curved hem",
      "Material & Care": ['Cotton', 'Machine-wash']
  },
      {
      "Image": ['3.1.jpg', '3.2.jpg', '3.3.jpg', '3.4.jpg'],
      "Brand": "Hire&Now",
      "Short Description": "Men Regular Fit Casual Shirt",
      "Description": "HERE&NOW Men Grey & Black Regular Fit Checked Casual Shirt",
      "Mrp": 1399,
      "Discount": 30,
      "Price": 979,
      "Size": {'38': 0, '40': 25, '42': 10, '44': 6},
      "Product Details": "Grey and black checked casual shirt, has a spread collar, button placket, 1 pocket, long sleeves, curved hem",
      "Material & Care": ['100% Cotton', 'Machine-wash']
  },
      {
      "Image": ['4.1.jpg', '4.2.jpg', '4.3.jpg', '4.4.jpg'],
      "Brand": "Nautica",
      "Short Description": "Men Regular Fit Casual Shirt",
      "Description": "Nautica Men Blue & Grey Regular Fit Checked Casual Shirt",
      "Mrp": 1499,
      "Discount": 65,
      "Price": 524,
      "Size": {'38': 0, '40': 25, '42': 10, '44': 6},
      "Product Details": "Blue and grey checked casual shir",
      "Material & Care": ['Linen', 'Machine-wash']
  },
      {
      "Image": ['20.1.jpg', '20.2.jpg', '20.3.jpg', '20.4.jpg'],
      "Brand": "Popnetic",
      "Type":"Shirt",
      "Category":"Women",
      "Seller":"Wiztech Corp",
      "Short Description": "Women Pink Straight Regular Fit Solid Casual Shirt",
      "Description": "Pink solid casual shirt, has a cutaway collar, button placket, na pockets, long sleeves, curved hem",
      "Mrp": 2759,
      "Discount": 40,
      "Price": 1000,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "Pink solid casual shirt, has a cutaway collar, button placket, na pockets, long sleeves, curved hem.Complete The Look - This cotton tee from Jaipur Kurti will add an extra layer of warmth to your outfit. Create a chic look for your next date by pairing this shirt with slim jeans and patent pumps",
      "Material & Care": ['Cotton', 'Hand-wash']
  },
      {
      "Image": ['21.1.jpg', '21.2.jpg', '21.3.jpg', '21.4.jpg'],
      "Brand": "La Zorie",
      "Type":"Top",
      "Category":"Women",
      "Seller":"Blumentor",
      "Short Description": "Women Dusty Pink Solid Top",
      "Description": "Dusty Pink solid woven regular top, has a tie-up neck, three-quarter sleeves",
      "Mrp": 699,
      "Discount": 10,
      "Price": 629,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "La Zorie Dusty Pink solid woven regular top, has a tie-up neck, three-quarter sleeves.Spruce up your wardrobe with this high-quality long-sleeve top from La Zoire. This pink top is a great addition to your cool-weather wardrobe and looks great with your favourite pair of jeans for a laid-back lunch date look.",
      "Material & Care": ['Linen', 'Machine-wash']
  },
      {
      "Image": ['22.1.jpg', '22.2.jpg', '22.3.jpg', '22.4.jpg'],
      "Brand": "Harpa",
      "Type":"Top",
      "Category":"Women",
      "Seller":"Blumentor",
      "Short Description": "Women Burgundy Solid Top",
      "Description": "Burgundy solid woven regular top, has a V-neck, three-quarter sleeves",
      "Mrp": 1199,
      "Discount": 55,
      "Price": 539,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "Harpa Burgundy solid woven regular top, has a V-neck, three-quarter sleeves.Increase your style quotient with this top-notch three-quarter sleeve top by Harpa. Grab a casual bite to eat outside in this burgundy piece with worn jeans and comfortable shoes.",
      "Material & Care": ['100% Polyester', 'Hand-wash']
  },
      {
      "Image": ['23.1.jpg', '23.2.jpg', '23.3.jpg', '23.4.jpg'],
      "Brand": "Libas",
      "Type":"Shirt",
      "Category":"Women",
      "Seller":"Mayazen",
      "Short Description": "Women Mustard Yellow Solid Casual Shirt With Embroidered Detail",
      "Description": "Mustard yellow solid casual shirt with embroidered detail, has a spread collar, a full button placket, three-quarter roll-up sleeves, high-low hem",
      "Mrp": 1399,
      "Discount": 50,
      "Price": 699,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "Libas Mustard yellow solid casual shirt with embroidered detail, has a spread collar, a full button placket, three-quarter roll-up sleeves, high-low hem. The three-quarter sleeves on this tee from Libas provides extra comfort and style. Pair yours with distressed denims and Chelsea boots and enjoy cocktails and dinner with your friends.",
      "Material & Care": ['Rayon', 'Hand-wash']
  },
      {
      "Image": ['24.1.jpg', '24.2.jpg', '24.3.jpg', '24.4.jpg'],
      "Brand": "Zima Leto",
      "Type":"Dress",
      "Category":"Women",
      "Seller":"Elixirnet",
      "Short Description": "Women Navy Blue Solid Midi Sheath Dress",
      "Description": "Navy blue solid knitted midi sheath dress, has a round neck, sleeveless, concealed zip and button closure, straight hem",
      "Mrp": 1099,
      "Discount": 40,
      "Price": 659,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "Zima Leto Navy blue solid knitted midi sheath dress, has a round neck, sleeveless, concealed zip and button closure, straight hem.Turn heads this season in this effortlessly stylish dress by Zima Leto. When you're going to an art gallery opening or the theater, wear this solid navy blue piece with platform heels and a trendy clutch.",
      "Material & Care": ['Polyester', 'Machine-wash']
  },
      {
      "Image": ['25.1.jpg', '25.2.jpg', '25.3.jpg', '25.4.jpg'],
      "Brand": "DressBerry",
      "Type":"Dress",
      "Category":"Women",
      "Seller":"Wiztech Corp",
      "Short Description": "Women Blue Solid Pinafore Dress",
      "Description": "Blue solid woven pinafore dress, has a square neck, sleeveless,flared hem",
      "Mrp": 1499,
      "Discount": 30,
      "Price": 1049,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "DressBerry Blue solid woven pinafore dress, has a square neck, sleeveless,flared hem. Make a name for yourself this season when you wear this DressBerry dress. The solid blue piece can be matched with patent pumps and a pretty purse when you have a semi-formal event to attend.",
      "Material & Care": ['Cotton', 'Machine-wash']
  },
      {
      "Image": ['26.1.jpg', '26.2.jpg', '26.3.jpg', '26.4.jpg'],
      "Brand": "Veni Vidi Vici",
      "Type":"Dress",
      "Category":"Women",
      "Seller":"Blumentor,
      "Short Description": "Women Maroon Solid Bardot Fit and Flare Dress",
      "Description": "Maroon solid knitted fit and flare dress, has off-shoulder styling, short sleeves, flared hem",
      "Mrp": 1890,
      "Discount": 30,
      "Price": 1323,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "Veni Vidi Vici Maroon solid knitted fit and flare dress, has off-shoulder styling, short sleeves, flared hem. You're sure to love the style and comfort of this lavish Veni Vidi Vici dress. Spruce up this solid maroon piece for work by layering it with a light sweater and some ballerinas.",
      "Material & Care": ['95% Polyester', 'Machine-wash']
  },
      {
      "Image": ['27.1.jpg', '27.2.jpg', '27.3.jpg', '27.4.jpg'],
      "Brand": "Harpa",
      "Type":"Dress",
      "Category":"Women",
      "Seller":"Blumentor",
      "Short Description": "Women Yellow Floral Print A-Line Dress",
      "Description": "Yellow floral print woven A-line dress with cut-out detail, has a round neck, three-quarter sleeves, button closure, slightly flared hem",
      "Mrp": 1499,
      "Discount": 55,
      "Price": 674,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "Harpa Yellow floral print woven A-line dress with cut-out detail, has a round neck, three-quarter sleeves, button closure, slightly flared hem. Show off your great sense of fashion when you opt for this Harpa dress. Wear this printed yellow piece with a pair of heels or flats for a perfect lunch look.",
      "Material & Care": ['100% Polyester', 'Hand-wash']
  },
      {
      "Image": ['28.1.jpg', '28.2.jpg', '28.3.jpg', '28.4.jpg'],
      "Brand": "Miss Chase",
      "Type":"Dress",
      "Category":"Women",
      "Seller":"FashionTech",
      "Short Description": "Women Navy Striped Detail T-shirt Dress",
      "Description": "Navy striped detail knit T-shirt dress, has a round neck, three-quarter sleeves, straight hem",
      "Mrp": 1499,
      "Discount": 55,
      "Price": 674,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "Miss Chase Navy striped detail knit T-shirt dress, has a round neck, three-quarter sleeves, straight hem. Showcase your great sense of fashion when you opt for this Miss Chase dress. Wear this navy piece with ballerinas and your favourite sweater for a cute date look.",
      "Material & Care": ['Cotton', 'Machine-wash']
  },
      {
      "Image": ['29.1.jpg', '29.2.jpg', '29.3.jpg', '29.4.jpg'],
      "Brand": "Athena",
      "Type":"",
      "Category":"",
      "Seller":"",
      "Short Description": "Women Navy Lace Sheath Dress",
      "Description": "Navy lace woven sheath dress, has a keyhole neck, three-quarter sleeves, concealed zip closure, an attached lining, straight hem",
      "Mrp": 2295,
      "Discount": 40,
      "Price": 1377,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "This timeless and elegant Athena dress is suitable for any season. Complement this piece with a pair of caged heels, your favourite bag and some minimalistic silver jewellery for a classy date ensemble.",
      "Material & Care": ['Nylon and Polyester blend', 'Hand-wash']
  }

  ])
mongo.db.items.insert_many([   {
      "Image": ['20.1.jpg', '20.2.jpg', '20.3.jpg', '20.4.jpg'],
      "Brand": "Popnetic",
      "Type":"Shirt",
      "Category":"Women",
      "Seller":"Wiztech Corp",
      "Short Description": "Women Pink Straight Regular Fit Solid Casual Shirt",
      "Description": "Pink solid casual shirt, has a cutaway collar, button placket, na pockets, long sleeves, curved hem",
      "Mrp": 2759,
      "Discount": 40,
      "Price": 1000,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "Pink solid casual shirt, has a cutaway collar, button placket, na pockets, long sleeves, curved hem.Complete The Look - This cotton tee from Jaipur Kurti will add an extra layer of warmth to your outfit. Create a chic look for your next date by pairing this shirt with slim jeans and patent pumps",
      "Material & Care": ['Cotton', 'Hand-wash']
  },
      {
      "Image": ['21.1.jpg', '21.2.jpg', '21.3.jpg', '21.4.jpg'],
      "Brand": "La Zorie",
      "Type":"Top",
      "Category":"Women",
      "Seller":"Blumentor",
      "Short Description": "Women Dusty Pink Solid Top",
      "Description": "Dusty Pink solid woven regular top, has a tie-up neck, three-quarter sleeves",
      "Mrp": 699,
      "Discount": 10,
      "Price": 629,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "La Zorie Dusty Pink solid woven regular top, has a tie-up neck, three-quarter sleeves.Spruce up your wardrobe with this high-quality long-sleeve top from La Zoire. This pink top is a great addition to your cool-weather wardrobe and looks great with your favourite pair of jeans for a laid-back lunch date look.",
      "Material & Care": ['Linen', 'Machine-wash']
  },
      {
      "Image": ['22.1.jpg', '22.2.jpg', '22.3.jpg', '22.4.jpg'],
      "Brand": "Harpa",
      "Type":"Top",
      "Category":"Women",
      "Seller":"Blumentor",
      "Short Description": "Women Burgundy Solid Top",
      "Description": "Burgundy solid woven regular top, has a V-neck, three-quarter sleeves",
      "Mrp": 1199,
      "Discount": 55,
      "Price": 539,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "Harpa Burgundy solid woven regular top, has a V-neck, three-quarter sleeves.Increase your style quotient with this top-notch three-quarter sleeve top by Harpa. Grab a casual bite to eat outside in this burgundy piece with worn jeans and comfortable shoes.",
      "Material & Care": ['100% Polyester', 'Hand-wash']
  },
      {
      "Image": ['23.1.jpg', '23.2.jpg', '23.3.jpg', '23.4.jpg'],
      "Brand": "Libas",
      "Type":"Shirt",
      "Category":"Women",
      "Seller":"Mayazen",
      "Short Description": "Women Mustard Yellow Solid Casual Shirt With Embroidered Detail",
      "Description": "Mustard yellow solid casual shirt with embroidered detail, has a spread collar, a full button placket, three-quarter roll-up sleeves, high-low hem",
      "Mrp": 1399,
      "Discount": 50,
      "Price": 699,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "Libas Mustard yellow solid casual shirt with embroidered detail, has a spread collar, a full button placket, three-quarter roll-up sleeves, high-low hem. The three-quarter sleeves on this tee from Libas provides extra comfort and style. Pair yours with distressed denims and Chelsea boots and enjoy cocktails and dinner with your friends.",
      "Material & Care": ['Rayon', 'Hand-wash']
  },
      {
      "Image": ['24.1.jpg', '24.2.jpg', '24.3.jpg', '24.4.jpg'],
      "Brand": "Zima Leto",
      "Type":"Dress",
      "Category":"Women",
      "Seller":"Elixirnet",
      "Short Description": "Women Navy Blue Solid Midi Sheath Dress",
      "Description": "Navy blue solid knitted midi sheath dress, has a round neck, sleeveless, concealed zip and button closure, straight hem",
      "Mrp": 1099,
      "Discount": 40,
      "Price": 659,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "Zima Leto Navy blue solid knitted midi sheath dress, has a round neck, sleeveless, concealed zip and button closure, straight hem.Turn heads this season in this effortlessly stylish dress by Zima Leto. When you're going to an art gallery opening or the theater, wear this solid navy blue piece with platform heels and a trendy clutch.",
      "Material & Care": ['Polyester', 'Machine-wash']
  },
      {
      "Image": ['25.1.jpg', '25.2.jpg', '25.3.jpg', '25.4.jpg'],
      "Brand": "DressBerry",
      "Type":"Dress",
      "Category":"Women",
      "Seller":"Wiztech Corp",
      "Short Description": "Women Blue Solid Pinafore Dress",
      "Description": "Blue solid woven pinafore dress, has a square neck, sleeveless,flared hem",
      "Mrp": 1499,
      "Discount": 30,
      "Price": 1049,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "DressBerry Blue solid woven pinafore dress, has a square neck, sleeveless,flared hem. Make a name for yourself this season when you wear this DressBerry dress. The solid blue piece can be matched with patent pumps and a pretty purse when you have a semi-formal event to attend.",
      "Material & Care": ['Cotton', 'Machine-wash']
  },
      {
      "Image": ['26.1.jpg', '26.2.jpg', '26.3.jpg', '26.4.jpg'],
      "Brand": "Veni Vidi Vici",
      "Type":"Dress",
      "Category":"Women",
      "Seller":"Blumentor",
      "Short Description": "Women Maroon Solid Bardot Fit and Flare Dress",
      "Description": "Maroon solid knitted fit and flare dress, has off-shoulder styling, short sleeves, flared hem",
      "Mrp": 1890,
      "Discount": 30,
      "Price": 1323,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "Veni Vidi Vici Maroon solid knitted fit and flare dress, has off-shoulder styling, short sleeves, flared hem. You're sure to love the style and comfort of this lavish Veni Vidi Vici dress. Spruce up this solid maroon piece for work by layering it with a light sweater and some ballerinas.",
      "Material & Care": ['95% Polyester', 'Machine-wash']
  },
      {
      "Image": ['27.1.jpg', '27.2.jpg', '27.3.jpg', '27.4.jpg'],
      "Brand": "Harpa",
      "Type":"Dress",
      "Category":"Women",
      "Seller":"Blumentor",
      "Short Description": "Women Yellow Floral Print A-Line Dress",
      "Description": "Yellow floral print woven A-line dress with cut-out detail, has a round neck, three-quarter sleeves, button closure, slightly flared hem",
      "Mrp": 1499,
      "Discount": 55,
      "Price": 674,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "Harpa Yellow floral print woven A-line dress with cut-out detail, has a round neck, three-quarter sleeves, button closure, slightly flared hem. Show off your great sense of fashion when you opt for this Harpa dress. Wear this printed yellow piece with a pair of heels or flats for a perfect lunch look.",
      "Material & Care": ['100% Polyester', 'Hand-wash']
  },
      {
      "Image": ['28.1.jpg', '28.2.jpg', '28.3.jpg', '28.4.jpg'],
      "Brand": "Miss Chase",
      "Type":"Dress",
      "Category":"Women",
      "Seller":"FashionTech",
      "Short Description": "Women Navy Striped Detail T-shirt Dress",
      "Description": "Navy striped detail knit T-shirt dress, has a round neck, three-quarter sleeves, straight hem",
      "Mrp": 1499,
      "Discount": 55,
      "Price": 674,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "Miss Chase Navy striped detail knit T-shirt dress, has a round neck, three-quarter sleeves, straight hem. Showcase your great sense of fashion when you opt for this Miss Chase dress. Wear this navy piece with ballerinas and your favourite sweater for a cute date look.",
      "Material & Care": ['Cotton', 'Machine-wash']
  },
      {
      "Image": ['29.1.jpg', '29.2.jpg', '29.3.jpg', '29.4.jpg'],
      "Brand": "Athena",
      "Type":"Dress",
      "Category":"Women",
      "Seller":"FashionTech",
      "Short Description": "Women Navy Lace Sheath Dress",
      "Description": "Navy lace woven sheath dress, has a keyhole neck, three-quarter sleeves, concealed zip closure, an attached lining, straight hem",
      "Mrp": 2295,
      "Discount": 40,
      "Price": 1377,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "This timeless and elegant Athena dress is suitable for any season. Complement this piece with a pair of caged heels, your favourite bag and some minimalistic silver jewellery for a classy date ensemble.",
      "Material & Care": ['Nylon and Polyester blend', 'Hand-wash']
  },{
      "Image": ['1.1.jpg', '1.2.jpg', '1.3.jpg', '1.4.jpg'],
      "Type": "Bedsheets",
      "Category": "Home & Living",
      "Brand": "SEJ by Nisha Gupta",
      "Seller": "Blumentor",
      "Color": "Cream",
      "Short Description": None,
      "Description": "SEJ by Nisha Gupta Cream-Coloured 240 TC Cotton Double Bedsheet with 2 Pillow Covers",
      "Mrp": 1999,
      "Discount": 55,
      "Price": 899,
      "Size": {'XXL': 100},
      "Product Details": "Set content: 1 bedsheet with 2 pillow covers \
                        Size: Double bed (king size)\
                        Quality: Fine, cotton\
                        Thread count: 240 TC\
                        Colour: Multicoloured\
                        Print/pattern: Floral\
                        Features: Flat",
      "Material & Care": ['100% cotton', 'Machine-wash'],
      "Complete The Look": "Revel in the comfort of a nice and cosy bed with the new collection of bedsheets from SEJ by Nisha Gupta. Styled with an enthralling design and pattern, it will flaunt the rich taste in your bed linen collection."
  },
  {
      "Image": ['2.1.jpg', '2.2.jpg', '2.3.jpg', '2.4.jpg'],
      "Type": "Bedsheet",
      "Category": "Home & Living",
      "Brand": "SEJ by Nisha Gupta",
      "Seller": "Blumentor",
      "Color": "Blue",
      "Short Description": None,
      "Description": "Blue Ethnic Motifs Flat 144 TC Cotton Double Bedsheet 2 Pillow Covers",
      "Mrp": 1399,
      "Discount": 50,
      "Price": 699,
      "Size": {'Double King': 100},
      "Product Details": "Set content: 1 King bedsheet with 2 pillow covers\
                            Quality: Regular\
                            Thread count: 144\
                            Colour: Blue and Mustard\
                            Pattern: Ethnic Motifs flat",
      "Material & Care": ['100% cotton', 'Machine-wash warm'],
      "Complete The Look": "The latest collection from SEJ by Nisha Gupta offers this premium and luxurious bedsheet. It will pull you out of lethargic atmosphere while creating an aura of serendipity and tranquillity."

  },
  {
      "Image": ['3.1.jpg', '3.2.jpg', '3.3.jpg', '3.4.jpg'],
      "Type": "Bedsheet",
      "Category": "Home & Living",
      "Brand": "SEJ by Nisha Gupta",
      "Seller": "Blumentor",
      "Color": "White",
      "Short Description": None,
      "Description": "White 160 TC Cotton Double Bedsheet with 2 Pillow Covers",
      "Mrp": 1399,
      "Discount": 50,
      "Price": 699,
      "Size": {'Double Queen': 100},
      "Product Details": "Set content: 1 bedsheet with 2 pillow covers\
                        Size: Double bed (king size)\
                        Quality: Regular, cotton\
                        Thread count: 160\
                        Features: Flat\
                        Colour: White\
                        Print/ pattern: Tropical print ",
"Material & Care": ['100% cotton', 'Machine-wash warm'],
"Complete The Look": "Add life and colours to your bedroom space with this trendy bedsheet. Styled with an enthralling design and pattern, it will flaunt your rich taste in exclusive bed linen. Made from 100% cotton fabric, it is skin-friendly, durable and easy to wash."

  },
  {
      "Image": ['4.1.jpg', '4.2.jpg', '4.3.jpg', '4.4.jpg'],
      "Type": "Bedsheet",
      "Category": "Home & Living",
      "Brand": "SEJ by Nisha Gupta",
      "Seller": "Blumentor",
      "Color": "White and Pink",
      "Short Description": None,
      "Description": "SEJ by Nisha Gupta White & Pink 160 TC Cotton Double Bedsheet with 2 Pillow Covers",
      "Mrp": 1399,
      "Discount": 50,
      "Price": 699,
      "Size": {'Double Queen': 100},
      "Product Details": "Set content: 1 bedsheet with 2 pillow covers\
                            Size: Double bed (king size)\
                            Quality: Regular, cotton\
                            Thread count: 160 TC\
                            Colour: White and pink\
                            Print/pattern: Tropical print\
                            Feature: Flat",
     "Material & Care": ['100% cotton', 'Machine-wash warm'],
      "Complete The Look": "Revel in the comfort of a nice and cosy bed with the new collection of bedsheets from SEJ by Nisha Gupta. Styled with an enthralling design and pattern, it will flaunt your rich taste in you bed linen collection."

  }, {
      "Image": ['5.1.jpg', '5.2.jpg', '5.3.jpg', '5.4.jpg'],
      "Type": "Bedsheet",
      "Category": "Home & Living",
      "Brand": "SEJ by Nisha Gupta",
      "Seller": "Blumentor",
      "Color": "Pink and Orange",
      "Short Description": None,
      "Description": "Pink & Orange 144 TC Cotton Double Bedsheet with 2 Pillow Covers",
      "Mrp": 1399,
      "Discount": 50,
      "Price": 699,
      "Size": {'Double Queen': 100},
      "Product Details": "Set content: 1 bedsheet with 2 pillow covers\
                        Size: Double bed (king size)\
                        Quality: Regular, cotton\
                        Thread count: 144\
                        Colours: Pink, orange and white\
                        Print: Geometric\
                        Feature: Flat",
     "Material & Care": ['100% cotton', 'Machine-wash warm'],
      "Complete The Look": "Revel in the comfort of a nice and cosy bed with the new collection of bedsheets from SEJ by Nisha Gupta. Styled with an enthralling design and pattern, it will leave your guests in awe."

  }, {
      "Image": ['6.1.jpg', '6.2.jpg', '6.3.jpg', '6.4.jpg'],
      "Type": "Bedsheet",
      "Category": "Home & Living",
      "Brand": "SEJ by Nisha Gupta",
      "Seller": "Blumentor",
      "Color": "Blue",
      "Short Description": None,
      "Description": "Blue Ethnic Motifs Flat 144 TC Cotton Double Bedsheet 2 Pillow Covers",
      "Mrp": 1999,
      "Discount": 55,
      "Price": 899,
      "Size": {'Double Queen': 100},
      "Product Details": "Set content: 1 bedsheet with 2 pillow covers\
                            Size: Double bed (king size)\
                            Quality: Regular, cotton\
                            Thread count: 180 TC\
                            Colours: Blue\
                            Print: Ethnic\
                            Feature: Flat",
     "Material & Care": ['100% cotton', 'Machine-wash warm'],
      "Complete The Look": "Revel in the comfort of a nice and cosy bed with the new collection of bedsheets from SEJ by Nisha Gupta. Styled with an enthralling design and pattern, it will leave your guests in awe."

  }, {
      "Image": ['7.1.jpg', '7.2.jpg', '7.3.jpg', '7.4.jpg'],
      "Type": "Bedsheet",
      "Category": "Home & Living",
      "Brand": "SEJ by Nisha Gupta",
      "Seller": "Blumentor",
      "Color": "Yellow and Orange",
      "Short Description": None,
      "Description": "Yellow & Orange 180 TC Cotton Double Bedsheet with 2 Pillow Covers",
      "Mrp": 1999,
      "Discount": 60,
      "Price": 799,
      "Size": {'Double Queen': 100},
      "Product Details": "Set content: 1 bedsheet with 2 pillow covers\
                        Size: Double bed (king size)\
                        Quality: Fine, cotton\
                        Thread count: 180\
                        Colour: Yellow and orange\
                        Print/ pattern: Abstract print",
      "Material & Care": ['100% cotton', 'Machine-wash cold'],
      "Complete The Look": "Add a splash of style to your bedroom with this brilliant bedsheet from SEJ by Nisha Gupta. The soft fabric is sure to give you a comfortable and undisturbed sleep."

  }, {
      "Image": ['8.1.jpg', '8.2.jpg', '8.3.jpg', '8.4.jpg'],
      "Type": "Bedsheet",
      "Category": "Home & Living",
      "Brand": "SEJ by Nisha Gupta",
      "Seller": "Blumentor",
      "Color": "White and Grey",
      "Short Description": None,
      "Description": "White & Grey Cotton 180 TC Double King Bedsheet with 2 Pillow Covers",
      "Mrp": 1999,
      "Discount": 55,
      "Price": 899,
      "Size": {'Double King': 100},
      "Product Details": "Set content: 1 bedsheet with 2 pillow covers\
                        Size: Double bed(king)\
                        Quality: Fine, cotton\
                        Thread count: 180 TC\
                        Feature: Flat\
                        Colour: White and grey\
                        Pattern: Conversational print",
      "Material & Care": ['100% cotton', 'Machine-wash warm'],
      "Complete The Look": "Crafted from premium quality cotton, this designer bedsheet from the house of SEJ by Nisha Gupta lends the luxurious feel and gives you a delightful sleep. Own it now and add a master-piece in your home linen collection."

  }, {
      "Image": ['9.1.jpg', '9.2.jpg', '9.3.jpg', '9.4.jpg'],
      "Type": "Bedsheet",
      "Category": "Home & Living",
      "Brand": "SEJ by Nisha Gupta",
      "Seller": "Blumentor",
      "Color": "Brown",
      "Short Description": None,
      "Description": "Multicoloured 240 TC Cotton Double Bedsheet with 2 Pillow Covers",
      "Mrp": 1999,
      "Discount": 55,
      "Price": 899,
      "Size": {'Double King': 100},
      "Product Details": "Set content: 1 bedsheet with 2 pillow covers\
                            Size: Double bed (queen size)\
                            Quality: Fine, cotton\
                            Thread count: 240\
                            Feature: Flat\
                            Colour: Multicoloured\
                            Print/ pattern: Floral",
      "Material & Care": ['100% cotton', 'Machine-wash cold'],
      "Complete The Look": "Add life and colours to your bed room space with this trendy bedsheet. Styled with an enthralling design and pattern, it will flaunt your rich taste in exclusive bed linen."

  },
  {
      "Image": ['10.1.jpg', '10.2.jpg', '10.3.jpg', '10.4.jpg'],
      "Type": "Bedsheet",
      "Category": "Home & Living",
      "Brand": "SEJ by Nisha Gupta",
      "Seller": "Blumentor",
      "Color": "White and Red",
      "Short Description": None,
      "Description": "White & Red Cotton 144 TC Double King Bedsheet With 2 Pillow Covers",
      "Mrp": 1999,
      "Discount": 55,
      "Price": 899,
      "Size": {'Double King': 100},
      "Product Details": "Set content: 1 bedsheet with 2 pillow covers\
                        Size: Double king\
                        Quality: Fine, Cotton\
                        Thread count: 144 TC\
                        Feature: Flat\
                        Colour: White, red and green\
                        Pattern: Floral print",
      "Material & Care": ['100% cotton', 'Machine-wash cold'],
      "Complete The Look": "Made from soft cotton fabric, this exclusive bedsheet from the house of SEJ by Nisha Gupta will make your nights comfortable and relaxed. The attractive prints and patterns will add a luxe touch to your bed linen collection."

  },
  {
      "Image": ['11.1.jpg', '11.2.jpg', '11.3.jpg'],
      "Type": "Bedsheet",
      "Category": "Home & Living",
      "Brand": "Portico New York",
      "Seller": "Blumentor",
      "Color": "Pink",
      "Short Description": None,
      "Description": "Pink Abstract Fitted 144 TC Cotton 1 Queen Bedsheet with 2 Pillow Covers",
      "Mrp": 1299,
      "Discount": 0,
      "Price": 1299,
      "Size": {'Double Queen': 100},
      "Product Details": "Set content: 1 Queen bedsheet with 2 pillow covers\
                        Quality: Regular\
                        Thread count: 144\
                        Colour: Pink\
                        Pattern: Abstract fitted",
      "Material & Care": ['100% cotton', 'Machine-wash cold'],
      "Complete The Look": "Made from soft cotton fabric, this exclusive bedsheet from the house of SEJ by Nisha Gupta will make your nights comfortable and relaxed. The attractive prints and patterns will add a luxe touch to your bed linen collection."

  },  # sold by blumentor(supplied by partner)
  {
      "Image": ['12.1.jpg', '12.2.jpg', '12.3.jpg'],
      "Type": "Bedsheet",
      "Category": "Home & Living",
      "Brand": "Portico New York",
      "Seller": "Blumentor",
      "Color": "White and Purple",
      "Short Description": None,
      "Description": "White & Purple Flat 144 TC Cotton 1 King Bedsheet with 2 Pillow Covers",
      "Mrp": 1799,
      "Discount": 0,
      "Price": 1799,
      "Size": {'Double King': 120},
      "Product Details": "Set content: 1 King bedsheet with 2 pillow covers\
                        Quality: Fine\
                        Thread count: 144\
                        Colour: White and Purple\
                        Pattern: Floral flat",
      "Material & Care": ['100% cotton', 'Machine-wash cold'],
      "Complete The Look": "Return home to the comfort of a nice and cosy bed with this bedsheet from Home Portico New York. Styled with an enthralling design and pattern, it will lend a fresh appeal to your bedroom."

  },{
      "Image": ['13.1.jpg', '13.2.jpg', '13.3.jpg'],
      "Type": "Bedsheet",
      "Category": "Home & Living",
      "Brand": "Portico New York",
      "Seller": "Blumentor",
      "Color": "Red",
      "Short Description": None,
      "Description": "Red & Off-White Ethnic Motifs Flat 144 TC Cotton 1 King Bedsheet with 2 Pillow Covers",
      "Mrp": 1899,
      "Discount": 0,
      "Price": 1899,
      "Size": {'Double King': 100},
      "Product Details": "Set content: 1 king bedsheet with 2 pillow covers\
                            Quality: fine\
                            Thread count: 144\
                            Colour: red and off-white\
                            Pattern: ethnic motifs flat",
      "Material & Care": ['100% cotton', 'Machine-wash cold'],
      "Complete The Look": "Return home to the comfort of a nice and cosy bed with this bedsheet from Home Portico New York. Styled with an enthralling design and pattern, it will lend a fresh appeal to your bedroom."

  }, {
      "Image": ['14.1.jpg', '14.2.jpg', '14.3.jpg'],
      "Type": "Bedsheet",
      "Category": "Home & Living",
      "Brand": "Trident",
      "Seller": "Elixirent",
      "Color": "Mustard Yellow",
      "Short Description": None,
      "Description": "Mustard Yellow Striped Flat 132 TC Cotton 1 Double Bedsheet with 2 Pillow Covers",
      "Mrp": 1499,
      "Discount": 55,
      "Price": 674,
      "Size": {'Double King': 140},
      "Product Details": "Set content: 1 Queen bedsheet with 2 pillow covers\
                            Quality: Regular\
                            Thread count: 132\
                            Colour: Mustard yellow and White\
                            Pattern: Striped flat",
      "Material & Care": ['100% cotton', 'Machine-wash cold'],
      "Complete The Look": "This sumptuous bedsheet by Trident will not only enhance the beauty of your room but will also aid in a satisfying sleep with its special Welsoft finish."  # sold by Elixirent

  },
  {
      "Image": ['15.1.jpg', '15.2.jpg', '15.3.jpg'],
      "Type": "Bedsheet",
      "Category": "Home & Living",
      "Brand": "Trident",
      "Seller": "Elixirent",
      "Color": "White & Blue",
      "Short Description": None,
      "Description": "White & Blue Floral Flat 120 TC Cotton 1 Queen Bedsheet with 2 Pillow Covers",
      "Mrp": 1199,
      "Discount": 50,
      "Price": 599,
      "Size": {'Double King': 140},
      "Product Details": "Set content: 1 Queen bedsheet with 2 pillow covers\
                            Quality: Regular\
                            Thread count: 132\
                            Colour: Mustard yellow and White\
                            Pattern: Striped flat",
      "Material & Care": ['100% cotton', 'Machine-wash cold'],
      "Complete The Look": "This sumptuous bedsheet by Trident will not only enhance the beauty of your room but will also aid in a satisfying sleep with its special Welsoft finish."  # sold by Elixirent

  },
  {
      "Image": ['16.1.jpg', '16.2.jpg', '16.3.jpg'],
      "Type": "Bedsheet",
      "Category": "Home & Living",
      "Brand": "Trident",
      "Seller": "Elixirent",
      "Color": "Grey & White",
      "Short Description": None,
      "Description": "Grey & White Floral Flat 144 TC Cotton 1 Queen Bedsheet with 2 Pillow Covers",
      "Mrp": 1499,
      "Discount": 55,
      "Price": 674,
      "Size": {'Double King': 140},
      "Product Details": "Set content: 1 Queen bedsheet with 2 pillow covers\
                        Quality: Regular\
                        Thread count: 132\
                        Colour: Mustard yellow and White\
                        Pattern: Striped flat",
      "Material & Care": ['100% cotton', 'Machine-wash cold'],
      "Complete The Look": "This sumptuous bedsheet by Trident will not only enhance the beauty of your room but will also aid in a satisfying sleep with its special Welsoft finish."  # sold by Elixirent

  },
   {
      "Image": ['17.1.jpg', '17.2.jpg', '17.3.jpg'],
      "Type": "Bedsheet",
      "Category": "Home & Living",
      "Brand": "Trident",
      "Seller": "Elixirent",
      "Color": "Green and Blue",
      "Short Description": None,
      "Description": "Green & Turquoise Blue 180 TC Cotton Double King Bedsheet with 2 Pillow Covers",
      "Mrp": 1499,
      "Discount": 55,
      "Price": 674,
      "Size": {'Double King': 140},
      "Product Details": "Set content: 1 Queen bedsheet with 2 pillow covers\
                        Quality: Regular\
                        Thread count: 132\
                        Colour:Green & Turquoise Blue\
                        Pattern: Striped flat",
      "Material & Care": ['100% cotton', 'Machine-wash'],
      "Complete The Look": "This sumptuous bedsheet by Trident will not only enhance the beauty of your room but will also aid in a satisfying sleep with its special Welsoft finish."  # sold by Elixirent

  },
  {
      "Image": ['18.1.jpg', '18.2.jpg', '18.3.jpg'],
      "Type": "Bedsheet",
      "Category": "Home & Living",
      "Brand": "Trident",
      "Seller": "Elixirent",
      "Color": "White and purple",
      "Short Description": None,
      "Description": "White & Purple Floral Flat 144 TC Cotton 1 Queen Bedsheet with 2 Pillow Covers",
      "Mrp": 2499,
      "Discount": 20,
      "Price": 1999,
      "Size": {'Double King': 140},
      "Product Details": "Set content: 1 Queen bedsheet with 2 pillow covers\
                        Quality: Regular\
                        Thread count: 132\
                        Colour: White & Purple\
                        Pattern: Striped flat",
      "Material & Care": ['100% cotton', 'Machine-wash '],
      "Complete The Look": "This sumptuous bedsheet by Trident will not only enhance the beauty of your room but will also aid in a satisfying sleep with its special Welsoft finish."  # sold by Elixirent

  },
  {
      "Image": ['19.1.jpg', '19.2.jpg', '19.3.jpg'],
      "Type": "Bedsheet",
      "Category": "Home & Living",
      "Brand": "Raymond Home",
      "Seller": "Elixirent",
      "Color": "Blue and White",
      "Short Description": None,
      "Description": "Blue & Off-White Geometric Flat 104 TC Cotton 1 King Bedsheet with 2 Pillow Covers",
      "Mrp": 1049,
      "Discount": 0,
      "Price": 1049,
      "Size": {'Double King': 140},
      "Product Details": "Set content: 1 King bedsheet with 2 pillow covers\
                            Quality: Coarse\
                            Thread count: 104\
                            Colour: Blue and Off-White\
                            Pattern: Geometric fla",
      "Material & Care": ['100% cotton', 'Machine-wash cold'],
      "Complete The Look": "This sumptuous bedsheet by Trident will not only enhance the beauty of your room but will also aid in a satisfying sleep with its special Welsoft finish."  # sold by Elixirent

  },
  {
      "Image": ['20.1.jpg', '20.2.jpg', '20.3.jpg'],
      "Type": "Bedsheet",
      "Category": "Home & Living",
      "Brand": "Raymond Home",
      "Seller": "Elixirent",
      "Color": "Yellow",
      "Short Description": None,
      "Description": "Multicoloured Abstract Flat 104 TC Cotton 1 King Bedsheet with 2 Pillow Covers",
      "Mrp": 1499,
      "Discount": 55,
      "Price": 674,
      "Size": {'Double King': 140},
      "Product Details": "Set content: 1 King bedsheet with 2 pillow covers\
                        Quality: Coarse\
                        Thread count: 104\
                        Colour: Multicoloured\
                        Pattern: Abstract flat",
      "Material & Care": ['100% cotton', 'Machine-wash'],
      "Complete The Look": "This sumptuous bedsheet by Raymond Home will not only enhance the beauty of your room but will also aid in a satisfying sleep with its special Welsoft finish."  # sold by Elixirent

  },
  {
      "Image": ['21.1.jpg', '21.2.jpg', '21.3.jpg'],
      "Type": "Bedsheet",
      "Category": "Home & Living",
      "Brand": "URBAN DREAM",
      "Seller": "Proleague",
      "Color": "Grey & Blue",
      "Short Description": None,
      "Description": "Grey & Blue Cartoon Characters Flat 210 TC Cotton 1 King Bedsheet with 2 Pillow Covers",
      "Mrp": 2499,
      "Discount": 35,
      "Price": 1625,
      "Size": {'Double King': 140},
      "Product Details": "Set content: 1 King bedsheet with 2 pillow covers\
                        Quality: Fine\
                        Thread count: 210\
                        Colour: Grey and Blue\
                        Pattern: Cartoon Characters flat",
      "Material & Care": ['100% cotton', 'Machine-wash cold'],
      "Complete The Look": "This sumptuous bedsheet by URBAN DREAM will not only enhance the beauty of your room but will also aid in a satisfying sleep with its special Welsoft finish."  # sold by Proleague

  },
      {"Image": ['22.1.jpg', '22.2.jpg', '22.3.jpg'],
      "Type": "Bedsheet",
      "Category": "Home & Living",
      "Brand": "URBAN DREAM",
      "Seller": "Proleague",
      "Color": "Blue",
      "Short Description": None,
      "Description": "Blue Cartoon Characters Flat 210 TC Cotton 1 Queen Bedsheet with 2 Pillow Covers",
      "Mrp": 2499,
      "Discount": 35,
      "Price": 1625,
      "Size": {'Double King': 140},
      "Product Details": "Set content: 1 King bedsheet with 2 pillow covers\
                        Quality: Fine\
                        Thread count: 210\
                        Colour: Blue\
                        Pattern: Cartoon Characters flat",
     "Material & Care": ['100% cotton', 'Machine-wash cold'],
      "Complete The Look": "This sumptuous bedsheet by URBAN DREAM will not only enhance the beauty of your room but will also aid in a satisfying sleep with its special Welsoft finish."  # sold by Proleague

  },
   {"Image": ['23.1.jpg', '23.2.jpg', '23.3.jpg'],
      "Type":"Bedsheet",
      "Category":"Home & Living",
      "Brand":"URBAN DREAM",
      "Seller":"Proleague",
      "Color":"Grey",
      "Short Description": None,
      "Description": "Grey Cartoon Characters Flat 210 TC Cotton 1 Single Bedsheet",
      "Mrp": 1999,
      "Discount": 30,
      "Price": 1399,
      "Size": {'Double King':140},
      "Product Details": "Set content: 1 King bedsheet with 2 pillow covers\
                        Quality: Fine\
                        Thread count: 210\
                        Colour: Grey\
                        Pattern: Cartoon Characters flat",
      "Material & Care": ['100% cotton', 'Machine-wash cold'],
      "Complete The Look":"This sumptuous bedsheet by URBAN DREAM will not only enhance the beauty of your room but will also aid in a satisfying sleep with its special Welsoft finish." #sold by Proleague

  },
  {
      "Image": ['24.1.jpg', '24.2.jpg', '24.3.jpg','24.4.jpg'],
      "Type":"Bedsheet",
      "Category":"Home & Living",
      "Brand":"SPACES",
      "Seller":"Unistand",
      "Color":"Yellow and Brown",
      "Short Description": None,
      "Description": "Yellow & Brown Abstract Flat 210 TC Cotton 1 King Bedsheet with 2 Pillow Coverss",
      "Mrp": 3799,
      "Discount": 50,
      "Price": 1899,
      "Size": {'Double King':140},
      "Product Details": "Set content: 1 King bedsheet with 2 pillow covers\
                        Quality: Superfine\
                        Thread count: 210\
                        Colour: Yellow and Brown\
                        Pattern: Abstract flat",
      "Material & Care": ['100% cotton', 'Machine-wash cold'],
      "Complete The Look":"Add a splash of style to your bedroom with this brilliant bedsheet from the Chic Chintz collection by SPACES. The soft fabric is sure to give you a comfortable and undisturbed sleep." #sold by Unistand

  },
  {
      "Image": ['25.1.jpg', '25.2.jpg', '25.3.jpg','25.4.jpg'],
      "Type":"Bedsheet",
      "Category":"Home & Living",
      "Brand":"SPACES",
      "Seller":"Unistand",
      "Color":"Brown",
      "Short Description": None,
      "Description": "Brown Geometric Flat 210 TC Cotton 1 King Bedsheet with 2 Pillow Covers",
      "Mrp": 3799,
      "Discount": 50,
      "Price": 1899,
      "Size": {'Double King':140},
      "Product Details": "Set content: 1 King bedsheet with 2 pillow covers\
                        Quality: Superfine\
                        Thread count: 210\
                        Colour: Brown\
                        Pattern: Abstract flat",
      "Material & Care": ['100% cotton', 'Machine-wash cold'],
      "Complete The Look":"Add a splash of style to your bedroom with this brilliant bedsheet from the Chic Chintz collection by SPACES. The soft fabric is sure to give you a comfortable and undisturbed sleep." #sold by Unistand

  },
  {
      "Image": ['24.1.jpg', '24.2.jpg', '24.3.jpg','24.4.jpg'],
      "Type":"Bedsheet",
      "Category":"Home & Living",
      "Brand":"SPACES",
      "Seller":"Unistand",
      "Color":"Red",
      "Short Description": None,
      "Description": "Red Abstract Flat 180 TC Cotton 1 King Bedsheet with 2 Pillow Covers",
      "Mrp": 3799,
      "Discount": 50,
      "Price": 1899,
      "Size": {'Double King':140},
      "Product Details": "Set content: 1 King bedsheet with 2 pillow covers\
                            Quality: Superfine\
                            Thread count: 210\
                            Colour: Red\
                            Pattern: Abstract flat",
      "Material & Care": ['100% cotton', 'Machine-wash cold'],
      "Complete The Look":"Add a splash of style to your bedroom with this brilliant bedsheet from the Chic Chintz collection by SPACES. The soft fabric is sure to give you a comfortable and undisturbed sleep." #sold by Unistand

  },
  {
      "Image": ['27.1.jpg', '27.2.jpg', '27.3.jpg','27.4.jpg'],
      "Type":"Bedsheet",
      "Seller":"Unistand",
      "Category":"Home & Living",
      "Brand":"SPACES",
      "Color":"Blue And White",
      "Short Description": None,
      "Description": "Blue & White Floral Flat 180 TC Cotton 1 King Bedsheet with 2 Pillow Covers",
      "Mrp": 2795,
      "Discount": 10,
      "Price": 2515,
      "Size": {'Double King':140},
      "Product Details": "Set content: 1 King bedsheet with 2 pillow covers\
                        Quality: Fine\
                        Thread count: 180\
                        Colour: Blue and White\
                        Pattern: Floral flat",
      "Material & Care": ['100% cotton', 'Machine-wash cold'],
      "Complete The Look":"This sumptuous bedsheet by SPACES will not only enhance the beauty of your room but will also aid in a satisfying sleep with its special Welsoft finish." #sold by Unistand

  }
])

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)
items = mongo.db.items
items.insert_one(i2)
pprint.pprint(items.find_one({"image": "2.2"}))
