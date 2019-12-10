import sys
# work around needed for if not using the system python (such as with anaconda python distrib)
#mod_path = '/System/Library/Frameworks/Python.framework/Versions/{0:}.{1:}/Extras/lib/python/PyObjC'.format( sys.version_info[0], sys.version_info[1] )
#sys.path.append(mod_path)

from html_content import header_content
from Foundation import NSAppleScript
from datetime import datetime

# create applescript code object
s = NSAppleScript.alloc().initWithSource_(
    'tell app "Safari" to {URL,name} of tabs of windows'
)

# execute AS obj, get return value
result,_ = s.executeAndReturnError_(None)

# since we said {URL,name} we should have two items
assert result.numberOfItems() == 2 

# find number of tabs based on number of groups in the URL set
num_windows = result.descriptorAtIndex_(1).numberOfItems()

# create a simple dictionary
tabs = dict(( 'window {0:}'.format(win_num), []) for win_num in range(1, num_windows+1) )

for page_idx,win_num in enumerate(tabs,start=1):

    urls   = [ result.descriptorAtIndex_(1).descriptorAtIndex_(page_idx).descriptorAtIndex_(tab_num).stringValue()
              for tab_num in xrange(1, result.descriptorAtIndex_(1).descriptorAtIndex_(page_idx).numberOfItems()+1 ) ]

    titles = [ result.descriptorAtIndex_(2).descriptorAtIndex_(page_idx).descriptorAtIndex_(tab_num).stringValue().encode('ascii','xmlcharrefreplace')
              for tab_num in xrange(1, result.descriptorAtIndex_(1).descriptorAtIndex_(page_idx).numberOfItems()+1 ) ]

    tabs[win_num] = zip(urls,titles)


now = datetime.now()
now_string = now.strftime("%d%m%Y_%H%M%S")
file_name = "backups/" + now_string + "_backup.html"

with open(file_name, 'w+') as f:
    f.write(header_content)
    f.write('\t\t<title>'+ now_string + ' Backup</title>\n\t</head>\n\n\t')
    f.write('<body>\n\t\t<header>\n\t\t\t<h1>Safari Tabs Saver</h1>\n')
    f.write('\t\t\t<p><em>Backed up on ' + now.strftime("%d %B %Y, %H:%M:%S") + '</em></p>\n')
    f.write('\t\t\t<p class="warning">Note: clicking open all tabs will open all of them in your current window!</p><br/>\n')
    f.write('\t\t\t<p>')
    for i in range(1, num_windows+1):
        f.write('<a href="#window_' + str(i) + '">Window ' + str(i) + '</a>')
        if i!=num_windows:
            f.write(' | ')
    f.write('</p>\n\t\t</header>\n')
    for i in range(1, num_windows+1):
        key = "window " + str(i)
        f.write('\n\t\t<div class="window" id="window_' + str(i)+'">\n')
        f.write('\t\t\t<h2>Window ' + str(i) + '</h2>\n')
        for url, title in tabs[key]:
            f.write('\t\t\t<p><a href="' + url + '" target="_blank" class="links_' +str(i)+'">' + title + '</a></p>\n')
        f.write('\t\t\t<h3 class="open_all" id="'+str(i)+'" >Open all tabs from this session</h3>\n')
        f.write('\t\t</div>\n')
    f.write('\n\t\t<footer><p><em>This was generated with zhuhanming\'s <a href="https://github.com/zhuhanming/safari-tabs-saver" target="_blank">Safari Tab Saver</a>.</em></p></footer>\n')
    f.write('\n\t</body>\n</html>')
    f.close()
