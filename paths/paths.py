import os
execute_path = os.path.abspath('')
# if running from local machine
browsers_json_local = os.path.abspath('..//..//')
# if running from jenkins
jenkins = os.path.abspath('..//..//..//')
browsers_json_remote = os.path.join(jenkins, r'.aerokube\selenoid\browsers.json')

