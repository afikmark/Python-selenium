import os

#
execute_path = os.path.abspath('')
# if running from local machine
local_profile = os.path.abspath('..//..//')
# if running from jenkins
jenkins = os.path.abspath('..//..//..//')
browsers_json = os.path.join(jenkins, r'.aerokube\selenoid\browsers.json')

