Manga-downloader
================

Downloads your favorite manga from mangahit.com

When running the script, it'll ask you for the name of the manga as well as the chapter number.
Simply add those, and it'll start downloading the manga for you as .jpeg files with the name pagex.jpg
where x can range from 1-20.
I've used the number 20, since most managas have less than 20 pages for a chapter.
However you can modify the range factor in the program to a number that you find necessary.

Please note, you'll need a pretty decent internet speed for downloading these images as they are high quality.
You're actually downloading the full resolution jpeg image instead of cropping or taking a screenshot of it.


The program need beautifulsoup.
To install beautifulsoup, the easiest way would be through the easy_install and just typing 'beautifulsoup4'
I used beautfulsoup to download the images on the page. 
My first approach was through selenium, but it proved to me more difficiult due to the addition of regular expressions to match the required image.

Please don't use this for any other site. The script is optimized for mangahit.com

I'll be sure to come back and update this program for a better experience/functionality.

If you have any doubts, mail me at prasanthlouis21@gmail.com
