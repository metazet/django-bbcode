::
: django-bbcode: README.txt
::

Django-bbcode
=============

* http://github.com/maaku/django-bbcode

DESCRIPTION
-----------

Django-bbcode is a BBCode (http://www.bbcode.org) implementation for Python/
Django.  It will convert strings with BBCode markup to their HTML equivalent.
It is based upon the BBRuby library, which provides similar functionality to
Ruby developers.

INSTALL
-------

Please see the file INSTALL.txt.

USAGE
-----

FIXME (replace Ruby documentation):

  require 'bb-ruby' # (only needed if installed as a gem)

BBRuby has been included directly into the String class for use on any string object:

  text = "[b]Here is some bold text[/b] followed by some [u]underlined text[/u]"
  output = text.bbcode_to_html
  text.bbcode_to_html!

BBRuby will auto-escape HTML tags.  To prevent this just pass false as the second param:

  output = text.bbcode_to_html({}, false)

Only allow certain tags:

  output = text.bbcode_to_html({}, true, :enable, :image, :bold, :quote)

Disable certain tags:

  output = text.bbcode_to_html({}, true, :disable, :image, :bold, :quote)

Alternative Direct usage:

  output = BBRuby.to_html(bbcode_markup)

Define your own translation, in order to be more flexible:

    my_blockquote = {
      'Quote' => [
        /\[quote(:.*)?=(.*?)\](.*?)\[\/quote\1?\]/mi,
        '<div class="quote"><p><cite>\2</cite></p><blockquote>\3</blockquote></div>',
        'Quote with citation',
        '[quote=mike]please quote me[/quote]',
        :quote
      ],      
    }
 
    text.bbcode_to_html(my_blockquote)

TAGS PROCESSED
--------------

The following is the list of BBCode tags processed by Django-bbcode and their
associated symbol for enabling/disabling them

* [b]               :bold
* [i]               :italics
* [u]               :underline
* [s]               :strikeout 
* [del]             :delete
* [ins]             :insert
* [code]            :code
* [size]            :size
* [color]           :color
* [ol]              :orderedlist
* [ul]              :unorderedlist
* [li]              :listitem    
* [*]               :listitem
* [list]            :listitem
* [list=1]          :listitem
* [list=a]          :listitem
* [dl]              :definelist
* [dt]              :defineterm
* [dd]              :definition
* [quote]           :quote
* [quote=source]    :quote
* [url=link]        :link
* [url]             :link
* [img size=]       :image
* [img=]            :image
* [img]             :image
* [youtube]         :video  
* [gvideo]          :video
* [email]           :email

::
: End of File
::
