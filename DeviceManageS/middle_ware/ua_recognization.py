from user_agents import parse


def choose_template(template_name):
    def _request(func):
        def __request(*args, **kwargs):
            wsgi_request = args[0]
            ua_string = wsgi_request.META.get('HTTP_USER_AGENT')
            # print ua_string
            user_agent = parse(ua_string)
            # print user_agent
            is_mobile = user_agent.is_mobile
            # print is_mobile
            if is_mobile:
                kwargs['template_name'] = 'mobile_' + template_name
            else:
                kwargs['template_name'] = template_name
            ret = func(*args, **kwargs)
            return ret
        return __request
    return _request
