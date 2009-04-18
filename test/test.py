#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# django-bbcode: test.py
##

import sys
sys.path.insert(0,'..')

from bbcode import util as bbcode
import unittest

class BBCodeTestCase(unittest.TestCase):
    def test_strong(self):
        self.assertEquals(
            '<strong>simple</strong>',
            bbcode.to_html('[b]simple[/b]'))
        self.assertEquals(
            '<strong>simple</strong>',
            bbcode.to_html('[b:7a9ca2c5c3]simple[/b:7a9ca2c5c3]'))
        self.assertEquals(
            "<strong>line 1<br />line 2</strong>",
            bbcode.to_html("[b:7a9ca2c5c3]line 1\nline 2[/b:7a9ca2c5c3]"))
        self.assertEquals(
            '<strong>1. text 1:</strong> text 2<br /><strong>2. text 3</strong>',
            bbcode.to_html("[b:post_uid0]1. text 1:[/b:post_uid0] text 2\n[b:post_uid0]2. text 3[/b:post_uid0]"))

    def test_em(self):
        self.assertEquals(
            '<em>simple</em>',
            bbcode.to_html('[i]simple[/i]'))
        self.assertEquals(
            '<em>simple</em>',
            bbcode.to_html('[i:7a9ca2c5c3]simple[/i:7a9ca2c5c3]'))
        self.assertEquals(
            "<em>line 1<br />line 2</em>",
            bbcode.to_html("[i:7a9ca2c5c3]line 1\nline 2[/i:7a9ca2c5c3]"))

    def test_u(self):
        self.assertEquals('<u>simple</u>', '[u]simple[/u]'.bbcode_to_html)
        self.assertEquals('<u>simple</u>', '[u:7a9ca2c5c3]simple[/u:7a9ca2c5c3]'.bbcode_to_html)
        self.assertEquals("<u>line 1<br />line 2</u>", "[u:7a9ca2c5c3]line 1\nline 2[/u:7a9ca2c5c3]".bbcode_to_html)

    def test_del(self):
        self.assertEquals('<del>simple</del>', '[del]simple[/del]'.bbcode_to_html)
        self.assertEquals('<del>simple</del>', '[del:7a9ca2c5c3]simple[/del:7a9ca2c5c3]'.bbcode_to_html)
        self.assertEquals('<del>simple</del>', '[s]simple[/s]'.bbcode_to_html)
        self.assertEquals('<del>simple</del>', '[s:7a9ca2c5c3]simple[/s:7a9ca2c5c3]'.bbcode_to_html)

    def test_ins(self):
        self.assertEquals('<ins>simple</ins>', '[ins]simple[/ins]'.bbcode_to_html)
        self.assertEquals('<ins>simple</ins>', '[ins:7a9ca2c5c3]simple[/ins:7a9ca2c5c3]'.bbcode_to_html)

    def test_code(self):
        self.assertEquals(
            '<code>simple</code>',
            bbcode.to_html('[code]simple[/code]'))
        self.assertEquals(
            '<code>simple</code>',
            bbcode.to_html('[code:7a9ca2c5c3]simple[/code:7a9ca2c5c3]'))
        self.assertEquals(
            "<code>var bxi = 0;<br />//Holds current speed of scrolling menu</code>",
            bbcode.to_html("[code:1:91cbdd72b7]var bxi = 0;\n//Holds current speed of scrolling menu[/code:1:91cbdd72b7]"))

    def test_size(self):
        self.assertEquals('<span style="font-size: 32px;">12px Text</span>', '[size=32]12px Text[/size]'.bbcode_to_html)
  
    def test_color(self):
        self.assertEquals('<span style="color: red;">Red Text</span>', '[color=red]Red Text[/color]'.bbcode_to_html)
        self.assertEquals('<span style="color: #ff0023;">Hex Color Text</span>', '[color=#ff0023]Hex Color Text[/color]'.bbcode_to_html)
        self.assertEquals('<span style="color: #B23803;">text</span>', '[color=#B23803:05d7c56429]text[/color:05d7c56429]'.bbcode_to_html)

    def test_ordered_list(self):
        self.assertEquals('<ol><li>item 1</li><li>item 2</li></ol>', '[ol][li]item 1[/li][li]item 2[/li][/ol]'.bbcode_to_html)
        self.assertEquals('<ol><li>item 1</li><li>item 2</li></ol>', '[ol][*]item 1[*]item 2[/ol]'.bbcode_to_html)

    def test_unordered_list(self):
        self.assertEquals('<ul><li>item 1</li><li>item 2</li></ul>', '[ul][li]item 1[/li][li]item 2[/li][/ul]'.bbcode_to_html)
        self.assertEquals('<ul><li>item 1</li><li>item 2</li></ul>', '[ul][*]item 1[*]item 2[/ul]'.bbcode_to_html)

    def test_list_unordered(self):
        self.assertEquals('<ul><li>item 1</li><li>item 2</li></ul>', '[list][li]item 1[/li][li]item 2[/li][/list]'.bbcode_to_html)
        self.assertEquals('<ul><li>item 1</li><li>item 2</li></ul>', '[list:7a9ca2c5c3][li]item 1[/li][li]item 2[/li][/list:o:7a9ca2c5c3]'.bbcode_to_html)
        self.assertEquals('<ul><li>item 1</li><li>item 2</li></ul><ul><li>item 3</li><li>item 4</li></ul>',
            '[list:7a9ca2c5c3][li]item 1[/li][li]item 2[/li][/list:o:7a9ca2c5c3][list:7a9ca2c5c3][li]item 3[/li][li]item 4[/li][/list:o:7a9ca2c5c3]'.bbcode_to_html)
        self.assertEquals('<ul><li>item 1</li><li>item 2</li></ul><ul><li>item 3</li><li>item 4</li></ul><ul><li>item 5</li><li>item 6</li></ul><ul><li>item 7</li><li>item 8</li></ul>',
            '[list:7a9ca2c5c3][li]item 1[/li][li]item 2[/li][/list:o:7a9ca2c5c3][list:7a9ca2c5c3][li]item 3[/li][li]item 4[/li][/list:o:7a9ca2c5c3][list:7a9ca2c5c3][li]item 5[/li][li]item 6[/li][/list:o:7a9ca2c5c3][list:7a9ca2c5c3][li]item 7[/li][li]item 8[/li][/list:o:7a9ca2c5c3]'.bbcode_to_html)

    def test_list_unordered_alternative(self):
        self.assertEquals('<li>item1</li><li>item2</li>', '[*:asdf]item1[*:asdf]item2'.bbcode_to_html)
        self.assertEquals('<ul><li>item1</li><li>item2</li></ul>', '[list:5d7cf5560a][*]item1[*]item2[/list:u:5d7cf5560a]'.bbcode_to_html)
        self.assertEquals('<ul><li>item1</li><li>item2</li></ul>', '[list:5d7cf5560a][*:5d7cf5560a]item1[*:5d7cf5560a]item2[/list:u:5d7cf5560a]'.bbcode_to_html)

    def test_list_ordered_numerically(self):
        self.assertEquals('<ol><li>item 1</li><li>item 2</li></ol>', '[list=1][li]item 1[/li][li]item 2[/li][/list]'.bbcode_to_html)
        self.assertEquals('<ol><li>item 1</li><li>item 2</li></ol>', '[list=1:7a9ca2c5c3][li]item 1[/li][li]item 2[/li][/list:7a9ca2c5c3]'.bbcode_to_html)

    def test_list_ordered_alphabetically(self):
        self.assertEquals('<ol sytle="list-style-type: lower-alpha;"><li>item 1</li><li>item 2</li></ol>', '[list=a][li]item 1[/li][li]item 2[/li][/list]'.bbcode_to_html)
        self.assertEquals('<ol sytle="list-style-type: lower-alpha;"><li>item 1</li><li>item 2</li></ol>', '[list=a:7a9ca2c5c3][li]item 1[/li][li]item 2[/li][/list:o:7a9ca2c5c3]'.bbcode_to_html)

    def test_two_lists(self):
        self.assertEquals('<ul><li>item1</li><li>item2</li></ul><ul><li>item1</li><li>item2</li></ul>',
            '[list:5d7cf5560a][*:5d7cf5560a]item1[*:5d7cf5560a]item2[/list:u:5d7cf5560a][list:5d7cf5560a][*:5d7cf5560a]item1[*:5d7cf5560a]item2[/list:u:5d7cf5560a]'.bbcode_to_html)

    def test_definition_list_term_definition(self):
        self.assertEquals('<dl><dt>term 1</dt><dd>definition 1</dd><dt>term 2</dt><dd>definition 2</dd></dl>', '[dl][dt]term 1[/dt][dd]definition 1[/dd][dt]term 2[/dt][dd]definition 2[/dd][/dl]'.bbcode_to_html)

    def test_quote(self):
        self.assertEquals('<fieldset><blockquote>quoting</blockquote></fieldset>', '[quote]quoting[/quote]'.bbcode_to_html)
        self.assertEquals('<fieldset><blockquote>quoting</blockquote></fieldset>', '[quote]quoting[/quote]'.bbcode_to_html.bbcode_to_html({}, False, 'disable'))
        self.assertEquals('<fieldset><legend>black</legend><blockquote>si el niño hubiera sido de "penalty" le hubieran llamado <strong>system Error</strong>!!! :)</blockquote></fieldset>', "[quote:7a9ca2c5c3=\"black\"]si el niño hubiera sido de \"penalty\" le hubieran llamado [b:7a9ca2c5c3]system Error[/b:7a9ca2c5c3]!!! :)[/quote:7a9ca2c5c3]".bbcode_to_html)
        self.assertEquals('<fieldset><legend>black</legend><blockquote>si el niño hubiera sido de "penalty" le hubieran llamado <strong>system Error</strong>!!! :)</blockquote></fieldset>', "[quote:7a9ca2c5c3=\"black\"]si el niño hubiera sido de \"penalty\" le hubieran llamado [b:7a9ca2c5c3]system Error[/b:7a9ca2c5c3]!!! :)[/quote:7a9ca2c5c3]".bbcode_to_html.bbcode_to_html({}, False, 'disable'))
        self.assertEquals('<fieldset><legend>Who</legend><blockquote>said that</blockquote></fieldset>', '[quote=Who]said that[/quote]'.bbcode_to_html)
        self.assertEquals('<fieldset><legend>Who</legend><blockquote>said that</blockquote></fieldset>', '[quote=Who]said that[/quote]'.bbcode_to_html.bbcode_to_html({}, false, 'disable'))

    def test_double_quote(self):
       self.assertEquals('<fieldset><legend>Kitten</legend><blockquote><fieldset><legend>creatiu</legend><blockquote>f1</blockquote></fieldset>f2</blockquote></fieldset>',
           '[quote:26fe26a6a9="Kitten"][quote:26fe26a6a9="creatiu"]f1[/quote:26fe26a6a9]f2[/quote:26fe26a6a9]'.bbcode_to_html.bbcode_to_html({}, false, 'disable'))

    def test_link(self):
        self.assertEquals('<a href="http://google.com">Google</a>', '[url=http://google.com]Google[/url]'.bbcode_to_html)
        self.assertEquals('<a href="http://google.com">http://google.com</a>', '[url]http://google.com[/url]'.bbcode_to_html)
        self.assertEquals('<a href="http://www.altctrlsupr.com/dmstk/kdd070803/00.html"> ABRIR ALBUM </a>','[URL=http://www.altctrlsupr.com/dmstk/kdd070803/00.html] ABRIR ALBUM [/URL]'.bbcode_to_html)
        self.assertEquals('<a href="http://www.altctrlsupr.com/dmstk/kdd070803/00.html"> ABRIR<br />ALBUM </a>',"[URL=http://www.altctrlsupr.com/dmstk/kdd070803/00.html] ABRIR\nALBUM [/URL]".bbcode_to_html)
        self.assertEquals('<a href="http://www.urimalet.com/cadaverex.mp3">aha</a>', "[URL=http://www.urimalet.com/cadaverex.mp3]aha[/URL]".bbcode_to_html)

    def test_image(self):
        self.assertEquals('<img src="http://zoople/hochzeit.png" alt="" />', '[img]http://zoople/hochzeit.png[/img]'.bbcode_to_html)
        self.assertEquals('<img src="http://zoople/hochzeit.png" alt="" />', '[img=http://zoople/hochzeit.png]'.bbcode_to_html)
        self.assertEquals('<img src="http://zoople/hochzeit.png" style="width: 95px; height: 96px;" />', '[img size=95x96]http://zoople/hochzeit.png[/img]'.bbcode_to_html)
        self.assertEquals('<img src="http://zoople/hochzeit.png" alt="" />', '[img:7a9ca2c5c3]http://zoople/hochzeit.png[/img:7a9ca2c5c3]'.bbcode_to_html)
        self.assertEquals('<img src="http://zoople/hochzeit.png" style="width: 95px; height: 96px;" />', '[img:7a9ca2c5c3 size=95x96]http://zoople/hochzeit.png[/img:7a9ca2c5c3]'.bbcode_to_html)
        self.assertEquals('<img src="http://www.marcodigital.com/sitanddie/sitanddiepequeÃ±o.jpg" alt="" />', '[img:post_uid0]http://www.marcodigital.com/sitanddie/sitanddiepequeÃ±o.jpg[/img:post_uid0]'.bbcode_to_html)

    def test_youtube(self):
        # Uncomment below if using 4:3 format youtube video embed
        # self.assertEquals('<object width="320" height="265"><param name="movie" value="http://www.youtube.com/v/E4Fbk52Mk1w"></param><param name="wmode" value="transparent"></param><embed src="http://www.youtube.com/v/E4Fbk52Mk1w" type="application/x-shockwave-flash" wmode="transparent" width="320" height="265"></embed></object>','[youtube]http://youtube.com/watch?v=E4Fbk52Mk1w[/youtube]'.bbcode_to_html)
        self.assertEquals('<object width="320" height="265"><param name="movie" value="http://www.youtube.com/v/E4Fbk52Mk1w"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed src="http://www.youtube.com/v/E4Fbk52Mk1w" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="320" height="265"></embed></object>', '[youtube]http://youtube.com/watch?v=E4Fbk52Mk1w[/youtube]'.bbcode_to_html)

    def test_google_video(self):
        self.assertEquals('<embed style="width:400px; height:326px;" id="VideoPlayback" type="application/x-shockwave-flash" src="http://video.google.com/googleplayer.swf?docId=-2200109535941088987" flashvars=""> </embed>', '[gvideo]http://video.google.com/videoplay?docid=-2200109535941088987[/gvideo]'.bbcode_to_html)

    def test_email(self):
        self.assertEquals('<a href="mailto:wadus@wadus.com">wadus@wadus.com</a>', '[email]wadus@wadus.com[/email]'.bbcode_to_html)

    def test_html_escaping(self):
        self.assertEquals("<strong>&lt;i&gt;foobar&lt;/i&gt;</strong>", '[b]<i>foobar</i>[/b]'.bbcode_to_html)
        self.assertEquals("<strong><i>foobar</i></strong>", '[b]<i>foobar</i>[/b]'.bbcode_to_html({}, False))
        self.assertEquals("1 is &lt; 2", '1 is < 2'.bbcode_to_html)
        self.assertEquals("1 is < 2", '1 is < 2'.bbcode_to_html({}, False))
        self.assertEquals("2 is &gt; 1", '2 is > 1'.bbcode_to_html)
        self.assertEquals("2 is > 1", '2 is > 1'.bbcode_to_html({}, False))

    def test_disable_tags(self):
        self.assertEquals("[b]foobar[/b]", "[b]foobar[/b]".bbcode_to_html({}, true, 'disable', 'bold'))
        self.assertEquals("[b]<em>foobar</em>[/b]", "[b][i]foobar[/i][/b]".bbcode_to_html({}, True, 'disable', 'bold'))
        self.assertEquals("[b][i]foobar[/i][/b]", "[b][i]foobar[/i][/b]".bbcode_to_html({}, True, 'disable', 'bold', 'italics'))

    def test_enable_tags(self):
        self.assertEquals("<strong>foobar</strong>", "[b]foobar[/b]".bbcode_to_html({}, true, 'enable', 'bold'))
        self.assertEquals("<strong>[i]foobar[/i]</strong>", "[b][i]foobar[/i][/b]".bbcode_to_html({}, True, 'enable', 'bold'))
        self.assertEquals("<strong><em>foobar</em></strong>", "[b][i]foobar[/i][/b]".bbcode_to_html({}, True, 'enable', 'bold', 'italics'))

#    def test_to_html_bang_method(self):
#        foo = "[b]foobar[/b]"
#        self.assertEquals("<strong>foobar</strong>", foo.bbcode_to_html!)
#        self.assertEquals("<strong>foobar</strong>", foo)

    def test_self_tag_list(self):
        self.assertEquals(30, BBRuby.tag_list.size)

    def test_redefinition_of_tag_html(self):
        mydef = {
            'Quote': [
                r"\[quote(:.*)?=\"?(.*?)\"?\](.*?)\[/quote\1?\]",
                '<div class="quote"><p><cite>\2</cite></p><blockquote>\3</blockquote></div>',
                'Quote with citation',
                nil,
                'quote'],
            'Image (Resized)': [
                r"\[img(:.+)? size=(['\"]?)(\d+)x(\d+)\2\](.*?)\[/img\1?\]",
                '<div class="post_image"><img src="\5" style="width: \3px; height: \4px;" /></div>',
                'Display an image with a set width and height', 
                '[img size=96x96]http://www.google.com/intl/en_ALL/images/logo.gif[/img]',
                'image'],
            'Image (Alternative)': [
                r"\[img=([^\[\]].*?)\.(png|bmp|jpg|gif|jpeg)\]",
                '<div class="post_image"><img src="\1.\2" alt="" /></div>',
                'Display an image (alternative format)', 
                '[img=http://myimage.com/logo.gif]',
                'image'],
            'Image': [
                r"\[img(:.+)?\]([^\[\]].*?)\.(png|bmp|jpg|gif|jpeg)\[/img\1?\]",
                '<div class="post_image"><img src="\2.\3" alt="" /></div>',
                'Display an image',
                'Check out this crazy cat: [img]http://catsweekly.com/crazycat.jpg[/img]',
                'image'],
        }
        self.assertEquals('<div class="quote"><p><cite>Who</cite></p><blockquote>said that</blockquote></div>', '[quote=Who]said that[/quote]'.bbcode_to_html(mydef))
        self.assertEquals('<div class="quote"><p><cite>flandepan</cite></p><blockquote>hola</blockquote></div>', '[quote:0fc8a224d2="flandepan"]hola[/quote:0fc8a224d2]'.bbcode_to_html(mydef))
        self.assertEquals('<div class="post_image"><img src="http://zoople/hochzeit.png" alt="" /></div>', '[img]http://zoople/hochzeit.png[/img]'.bbcode_to_html(mydef))

    def test_multiple_tag_test(self):
        self.assertEquals("<strong>bold</strong><em>italic</em><u>underline</u><fieldset><blockquote>quote</blockquote></fieldset><a href=\"foobar\">link</a>", "[b]bold[/b][i]italic[/i][u]underline[/u][quote]quote[/quote][url=foobar]link[/url]".bbcode_to_html)
        self.assertEquals("<strong>bold</strong><em>italic</em><u>underline</u><fieldset><blockquote>quote</blockquote></fieldset><a href=\"foobar\">link</a>", "[b]bold[/b][i]italic[/i][u]underline[/u][quote]quote[/quote][url=foobar]link[/url]".bbcode_to_html({}, True, 'enable', 'bold', 'italics', 'underline', 'link', 'quote'))

    def test_no_ending_tag(self):
        self.assertEquals("this [b]should not be bold", "this [b]should not be bold".bbcode_to_html)

    def test_no_start_tag(self):
        self.assertEquals("this should not be bold[/b]", "this should not be bold[/b]".bbcode_to_html)

    def test_different_start_and_ending_tags(self):
        self.assertEquals("this [b]should not do formatting[/i]", "this [b]should not do formatting[/i]".bbcode_to_html)

if __name__ == '__main__':
    unittest.main()

##
# End of File
##
