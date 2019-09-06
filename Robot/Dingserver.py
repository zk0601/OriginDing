import requests
import json

Level_range = {'DEBUG': 4, 'INFO': 3, 'WARNING': 2, 'ERROR': 1}
Type_range = ['text', 'markdown']


class Dingserver(object):
    _type = 'text'
    _level = 'INFO'
    _at_all = False
    _at_users = []

    def __init__(self, access_token):
        self.access_token = access_token
        self.url = 'https://oapi.dingtalk.com/robot/send?access_token=%s' % access_token

    def config(self, **kwargs):
        if 'level' in kwargs and kwargs['level'] in Level_range:
            self._level = kwargs['level']
        if 'type' in kwargs and kwargs['type'] in Type_range:
            self._type = kwargs['type']
        if 'at_all' in kwargs and kwargs['at_all'] in (True, False):
            self._at_all = kwargs['at_all']
        if 'at_users' in kwargs:
            self._at_users = kwargs['at_users']

    def debug(self, content, **kwargs):
        if Level_range[self._level] >= Level_range['DEBUG']:
            return self._send_msg(content, **kwargs)

    def info(self, content, **kwargs):
        if Level_range[self._level] >= Level_range['INFO']:
            return self._send_msg(content, **kwargs)

    def warning(self, content, **kwargs):
        if Level_range[self._level] >= Level_range['WARNING']:
            return self._send_msg(content, **kwargs)

    def error(self, content, **kwargs):
        if Level_range[self._level] >= Level_range['ERROR']:
            return self._send_msg(content, **kwargs)

    def _send_msg(self, content, **kwargs):
        post_data = {}
        headers = {'content-type': 'application/json'}
        if 'type' in kwargs and kwargs['type'] in Type_range:
            msg_type = kwargs['type']
        else:
            msg_type = self._type
        if 'at_all' in kwargs and kwargs['at_all'] in (True, False):
            at_all = kwargs['at_all']
        else:
            at_all = self._at_all
        if 'at_users' in kwargs:
            at_users = kwargs['at_users']
        else:
            at_users = self._at_users

        if msg_type == 'text':
            post_data = {
                "msgtype": "text",
                "text": {
                    "content": content
                },
                "at": {
                    "atMobiles": at_users,
                    "isAtAll": at_all
                }
            }
        elif msg_type == 'markdown':
            post_data = {
                 "msgtype": "markdown",
                 "markdown": {
                     "title": "title",
                     "text": content
                 },
                "at": {
                    "atMobiles": at_users,
                    "isAtAll": at_all
                }
             }
        try:
            post_data = json.dumps(post_data)
            rs = requests.post(self.url, data=post_data, headers=headers)
            if rs.status_code == 200:
                if not json.loads(rs.content)["errcode"] == 0:
                    # print json.loads(rs.content)["errmsg"]
                    pass
            else:
                # print something wrong
                pass
        except:
            # print something wrong
            pass


if __name__ == '__main__':
    a = Dingserver('43b44717c59d1eba4ba7f4eb018d06b8962cf2178b029c37ec0b58365381d19c')
    a.config(level='WARNING', at_users=['15927260404'])
    a.error('### helloworld', type='markdown')
