
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
      "Image": [ '5.1.jpg', '5.2.jpg', '5.3.jpg', '5.4.jpg' ],
      "Brand": "GAP",
      "Short Description": "Pattern Oxford Shirt",
      "Description": "Men's Maroon Pattern Oxford Shirt In Stretch",
      "Mrp": 2499,
      "Discount": 10 ,
      "Price": 2249,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "GAP is one of the world's most iconic apparel and accessories brands and the authority on American casual style. Today, GAP continues to be the best destination for wardrobe essentials such as denim, tees, hoodies and great-fitting pants.Smooth, stretch oxford weave. Long sleeves with button cuffs. Button collar, button front. Patch pocket at chest. Curved shirttail hem",
      "Material & Care": ['98% Cotton, 2% Spandex', 'Machine wash cold']
  },
  {
      "Image": [ '6.1.jpg', '6.2.jpg', '6.3.jpg', '6.4.jpg' ],
      "Brand": "GAP",
      "Short Description": "Black Oxford Shirt",
      "Description": "Men's Black Pattern Oxford Shirt In Stretch",
      "Mrp": 2499,
      "Discount": 10,
      "Price": 2249,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "GAP is one of the world's most iconic apparel and accessories brands and the authority on American casual style. Today, GAP continues to be the best destination for wardrobe essentials such as denim, tees, hoodies and great-fitting pants.Smooth, stretch oxford weave. Long sleeves with button cuffs. Button collar, button front. Patch pocket at chest.Curved shirttail hem",
      "Material & Care": ['98% Cotton, 2% Spandex', 'Machine wash cold']
  },
  {
      "Image": [ '7.1.jpg', '7.2.jpg', '7.3.jpg', '7.4.jpg' ],
      "Brand": "GAP",
      "Short Description": "Striped Polo T Shirt",
      "Description": "Men's Grey Striped Polo Tshirt",
      "Mrp": 1499,
      "Discount": 10,
      "Price": 1349,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "Short sleeves, flat rib-knit cuffs. Flat rib-knit polo collar, button placket. Side seam vents at hem. Allover stripes",
      "Material & Care": ['100% Cotton ', 'Machine-wash']
  },
  {
      "Image": [ '8.1.jpg', '8.2.jpg', '8.3.jpg', '8.4.jpg' ],
      "Brand": "GAP",
      "Short Description": "Slim Fit Denim Western Shirt",
      "Description": "Men's Blue Slim Fit Denim Western Shirt",
      "Mrp": 3799,
      "Discount": 10,
      "Price": 3419,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "Premium, lightweight denim with low-stretch.Dark indigo wash with subtle fading and whiskering.Long sleeves, snap-button cuffs.Spread collar, snap-button front.Flap-patch pockets at chest with snap-button closure.Curved shirttail hem, vents at sides",
      "Material & Care": ['79% Cotton, 20% polyester, 1% Spandex', 'Hand-wash']
  },
  {
      "Image": [ '9.1.jpg', '9.2.jpg', '9.3.jpg', '9.4.jpg' ],
      "Brand": "GAP",
      "Short Description": "Poplin Shirt in Stretch",
      "Description": "Men's Brown & White Pattern Poplin Shirt in Stretch",
      "Mrp": 2499,
      "Discount": 10,
      "Price": 2249,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "GAP is one of the world's most iconic apparel and accessories brands and the authority on American casual style. Today, GAP continues to be the best destination for wardrobe essentials such as denim, tees, hoodies and great-fitting pants.",
      "Material & Care": ['95% Cotton, 5% Spandex', 'Hand-wash']
  },
  {
      "Image": [ '10.1.jpg', '10.2.jpg', '10.3.jpg', '10.4.jpg' ],
      "Brand": "GAP",
      "Short Description": "Striped Logo Tee",
      "Description": "Men's Blue & White Striped Logo Tee",
      "Mrp": 1499,
      "Discount": 10,
      "Price": 1349,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "GAP is one of the world's most iconic apparel and accessories brands and the authority on American casual style. Today, GAP continues to be the best destination for wardrobe essentials such as denim, tees, hoodies and great-fitting pants.",
      "Material & Care": ['100% Cotton', 'Machine-wash']
  },
  {
      "Image": ['20.1.jpg', '20.2.jpg', '20.3.jpg', '20.4.jpg'],
      "Brand": "Elixirnet",
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
      "Image": ['21.1.jpg', '21.2.jpg', '21.3.jpg', '21.4.jpg' ],
      "Brand": "La Zorie",
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
      "Image": [ '22.1.jpg', '22.2.jpg', '22.3.jpg', '22.4.jpg' ],
      "Brand": "Harpa",
      "Short Description": "Women Burgundy Solid Top",
      "Description": "Burgundy solid woven regular top, has a V-neck, three-quarter sleeves",
      "Mrp": 1199,
      "Discount": 55,
      "Price": 539,
      "Size": { 'S': 0, 'M': 25, 'L': 10, 'XL': 6 },
      "Product Details": "Harpa Burgundy solid woven regular top, has a V-neck, three-quarter sleeves.Increase your style quotient with this top-notch three-quarter sleeve top by Harpa. Grab a casual bite to eat outside in this burgundy piece with worn jeans and comfortable shoes.",
      "Material & Care": ['100% Polyester', 'Hand-wash']
  },
  {
      "Image": [ '23.1.jpg', '23.2.jpg', '23.3.jpg', '23.4.jpg' ],
      "Brand": "Libas",
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
      "Image": [ '24.1.jpg', '24.2.jpg', '24.3.jpg', '24.4.jpg' ],
      "Brand": "Zima Leto",
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
      "Image": [ '25.1.jpg', '25.2.jpg', '25.3.jpg', '25.4.jpg' ],
      "Brand": "DressBerry",
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
      "Image": [ '26.1.jpg', '26.2.jpg', '26.3.jpg', '26.4.jpg' ],
      "Brand": "Veni Vidi Vici",
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
      "Image": [ '27.1.jpg', '27.2.jpg', '27.3.jpg', '27.4.jpg' ],
      "Brand": "Harpa",
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
      "Image": [ '28.1.jpg', '28.2.jpg', '28.3.jpg', '28.4.jpg' ],
      "Brand": "Miss Chase",
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
      "Image": [ '29.1.jpg', '29.2.jpg', '29.3.jpg', '29.4.jpg' ],
      "Brand": "Athena",
      "Short Description": "Women Navy Lace Sheath Dress",
      "Description": "Navy lace woven sheath dress, has a keyhole neck, three-quarter sleeves, concealed zip closure, an attached lining, straight hem",
      "Mrp": 2295,
      "Discount": 40,
      "Price": 1377,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "This timeless and elegant Athena dress is suitable for any season. Complement this piece with a pair of caged heels, your favourite bag and some minimalistic silver jewellery for a classy date ensemble.",
      "Material & Care": ['Nylon and Polyester blend', 'Hand-wash']
  },
  {
      "Image": [ '30.1.jpg', '30.2.jpg', '30.3.jpg', '30.4.jpg' ],
      "Brand": "Harpa",
      "Short Description": "Solid Peplum Top",
      "Description": "Women Black Solid Peplum Top",
      "Mrp": 1399,
      "Discount": 60,
      "Price": 559,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "Black solid knitted peplum top, has a round neck, short sleeves, concealed zip closure",
      "Material & Care": ['Polyester', 'Hand-wash']
  },
   {
      "Image": [ '31.1.jpg', '31.2.jpg', '31.3.jpg', '31.4.jpg' ],
      "Brand": "Harpa",
      "Short Description": "Yellow Top",
      "Description": "Mustard Yellow Top",
      "Mrp": 999,
      "Discount": 55,
      "Price": 449,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "Mustard yellow woven top, has a V-neck, flared short sleeves, snap-button closures and elasticated detail on the back",
      "Material & Care": ['100% Polyester', 'Hand-wash']
  },
  {
      "Image": [ '32.1.jpg', '32.2.jpg', '32.3.jpg', '32.4.jpg' ],
      "Brand": "Harpa",
      "Short Description": "Printed Top",
      "Description": "Women Cream-Coloured Printed Top",
      "Mrp": 1199,
      "Discount": 60,
      "Price": 479,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "Cream-coloured printed woven regular top, has a round neck, three-quarter sleeves",
      "Material & Care": ['Polyester', 'Hand-wash']
  },
  {
      "Image": [ '33.1.jpg', '33.2.jpg', '33.3.jpg', '33.4.jpg' ],
      "Brand": "Niza",
      "Short Description": "Floral Printed Top",
      "Description": "Women White Floral Print Top",
      "Mrp": 4792,
      "Discount": 60,
      "Price": 1916,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "White floral print woven regular top, has a round neck, short sleeves.",
      "Material & Care": ['Polycotton', 'Machine-wash']
  },
  {
      "Image": [ '34.1.jpg', '34.2.jpg', '34.3.jpg', '34.4.jpg' ],
      "Brand": "Niza",
      "Short Description": "Floral Printed Boxy Top",
      "Description": "Women Blue Floral Print Boxy Top",
      "Mrp": 5592,
      "Discount": 60,
      "Price": 2236,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "Blue floral print woven boxy top, has a V-neck, short sleeves, button closure",
      "Material & Care": ['Polycotton', 'Machine-wash']
  },
  {
      "Image": [ '35.1.jpg', '35.2.jpg', '35.3.jpg', '35.4.jpg' ],
      "Brand": "Niza",
      "Short Description": "Self Design TOp",
      "Description": "Women Black Self Design Top",
      "Mrp": 4792,
      "Discount": 60,
      "Price": 1916,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "Black self-design knitted regular top, has a V-neck, three-quarter sleeves",
      "Material & Care": ['100% Cotton', 'Machine-wash']
  }
 
  ])
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)
items = mongo.db.items
items.insert_one(i2)
pprint.pprint(items.find_one({"image": "2.2"}))
