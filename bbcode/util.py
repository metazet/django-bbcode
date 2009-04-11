
# Convert a string with BBCode markup into its corresponding HTML markup
#
# === Basic Usage
#
# The first parameter is the string off BBCode markup to be processed
#
#   text = "[b]some bold text to markup[/b]"
#   output = BBRuby.to_html(text)
#   # output => "<strong>some bold text to markup</strong>"
#
# === Custom BBCode translations
#
# You can supply your own BBCode markup translations to create your own custom markup
# or override the default BBRuby translations (parameter is a hash of custom translations).
#
# The hash takes the following format: "name" => [regexp, replacement, description, example, enable_symbol]
#
#  custom_blockquote = {
#    'Quote' => [
#      /\[quote(:.*)?=(.*?)\](.*?)\[\/quote\1?\]/mi,
#      '<div class="quote"><p><cite>\2</cite></p><blockquote>\3</blockquote></div>',
#      'Quote with citation',
#      '[quote=mike]please quote me[/quote]',
#      :quote
#    ]
#  }
#
# === Enable and Disable specific tags
#
# BBRuby will allow you to only enable certain BBCode tags, or to explicitly disable certain tags.
# Pass in either :disable or :enable to set your method, followed by the comma-separated list of tags
# you wish to disable or enable
#
#   BBRuby.to_html(text, {}, true, :enable, :image, :bold, :quote)
#   BBRuby.to_html(text, {}, true, :disable, :image, :video, :color)
#
def to_html(text, tags_alternative_definition = {}, escape_html=true, method=:disable, *tags)
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

# Returns the list of tags processed by BBRuby in a Hash object
def tag_list
    @@tags

# Convert a string with BBCode markup into its corresponding HTML markup
#
# === Basic Usage
#
#   text = "[b]some bold text to markup[/b]"
#   output = text.bbcode_to_html
#   # output => "<strong>some bold text to markup</strong>"
#
# === Custom BBCode translations
#
# You can supply your own BBCode markup translations to create your own custom markup
# or override the default BBRuby translations (parameter is a hash of custom translations).
#
# The hash takes the following format: "name" => [regexp, replacement, description, example, enable_symbol]
#
#  custom_blockquote = {
#    'Quote' => [
#      /\[quote(:.*)?=(.*?)\](.*?)\[\/quote\1?\]/mi,
#      '<div class="quote"><p><cite>\2</cite></p><blockquote>\3</blockquote></div>',
#      'Quote with citation',
#      '[quote=mike]please quote me[/quote]',
#      :quote
#    ]
#  }
#
#  output = text.bbcode_to_html(custom_blockquote)
#
# === Enable and Disable specific tags
#
# BBRuby will allow you to only enable certain BBCode tags, or to explicitly disable certain tags.
# Pass in either :disable or :enable to set your method, followed by the comma-separated list of tags
# you wish to disable or enable
#
#   output = text.bbcode_to_html({}, true, :enable, :image, :bold, :quote)
#   output = text.bbcode_to_html({}, true, :disable, :image, :video, :color)
#
# === HTML auto-escaping
#
# By default, BBRuby will auto-escape HTML.  You can prevent this by passing in false as the second
# parameter
#
#   output = text.bbcode_to_html({}, false)
#
def bbcode_to_html(tags_alternative_definition = {}, escape_html=true, method=:disable, *tags)
    BBRuby.to_html(self, tags_alternative_definition, escape_html, method, tags)

# Replace the string contents with the HTML-converted markup
def bbcode_to_html!(tags_alternative_definition = {}, escape_html=true, method=:disable, *tags)
    self.replace(BBRuby.to_html(self, tags_alternative_definition, escape_html, method, tags))
