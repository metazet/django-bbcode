#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# django-bbcode: util.py
##

def to_html(text,
            tags_alternative_definition={},
            escape_html=true,
            method='disable',
            *tags):
    """
    Convert a string with BBCode markup into its corresponding HTML markup.

    Basic Usage
    -----------

    The first parameter is the string off BBCode markup to be processed

        >>> text = "[b]some bold text to markup[/b]"
        >>> output = bbcode.util.to_html(text)
        >>> print output
        <strong>some bold text to markup</strong>

    Custom BBCode translations
    --------------------------

    You can supply your own BBCode markup translations to create your own
    custom markup, or override the default BBRuby translations (parameter is a
    dictionary of custom translations).

    The dictionary takes the following format:

        "name": [regexp, replacement, description, example, enable_symbol]

    For example,

       custom_blockquote = {
           'Quote': [
               "\[quote(:.*)?=(.*?)\](.*?)\[\/quote\1?\]",
               '<div class="quote"><p><cite>\2</cite></p><blockquote>\3</blockquote></div>',
               'Quote with citation',
               '[quote=mike]please quote me[/quote]',
               'quote' ],
       }

    Enable and Disable specific tags
    --------------------------------

    Django-bbcode will allow you to only enable certain BBCode tags, or to
    explicitly disable certain tags.  Pass in either 'disable' or 'enable' to
    set your method, followed by the comma-separated list of tags you wish to
    disable or enable.

        ##
        # Translate BBCode to HTML, enabling 'image', 'bold', and 'quote' tags
        # *only*.
        bbcode.util.to_html(text, {}, true,
                            'enable',  'image', 'bold',  'quote')

        ##
        # Translate BBCode to HTML, enabling all tags *except* 'image',
        # 'bold', and 'quote'.
        bbcode.util.to_html(text, {}, true,
                            'disable', 'image', 'video', 'color')
    """
    text = text.clone
      
    # escape < and > to remove any html
    if escape_html
      text.gsub!( '&', '&amp;' )
      text.gsub!( '<', '&lt;' )
      text.gsub!( '>', '&gt;' )
    end
      
    tags_definition = @@tags.merge(tags_alternative_definition)

    # parse bbcode tags
    case method
        when :enable
            tags_definition.each_value { |t| text.gsub!(t[0], t[1]) if tags.include?(t[4]) }
        when :disable
            # this works nicely because the default is disable and the default set of tags is [] (so none disabled) :)
            tags_definition.each_value { |t| text.gsub!(t[0], t[1]) unless tags.include?(t[4]) }
    end

    # parse spacing
    text.gsub!( /\r\n?/, "\n" )
    text.gsub!( /\n/, "<br />\n" )

    # return markup
    text

##
# End of File
##
