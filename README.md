# image_scraping-Opals

This code scraps opal images from whole 'Solid opals' option. Only 'requests' library was used. Images were accessed by website's API.
Each saved image has added name and price, seperated by ' ; ' sign (for excel purpose).

You can then use AHK script to paste each image+name into new excel file, go to:  https://github.com/mban1993/images_to_excel

You have a folder named 'opals', where are all opal images stored (and only images you want to paste into excel file!).
![OPALS1](https://user-images.githubusercontent.com/118799677/205039184-59e370a2-19a1-4584-b2a4-bebe92008f5f.jpg)

Use one of AHK scripts - one pastes small-sized images, second one pastes larger images. Select folder 'opals'. After that, new excel file should be opened
with list of opals and their names.
![opals2](https://user-images.githubusercontent.com/118799677/205039640-8613e250-0221-4b2b-8659-e448cfae506e.jpg)

You might want to split name and price - we'll use ' ; ' sign to have name in one column, and price in second column. In Excel:
1) Data > Text to Columns
2) In the Convert Text to Columns Wizard, select Delimited > Next
3) Select ' ; ' sign as delimiter.

After some formatting we have a list of opal images, names and their prices.
![opals3](https://user-images.githubusercontent.com/118799677/205040463-861aa2d3-6ceb-4652-86b8-53bbbabd1535.jpg)
