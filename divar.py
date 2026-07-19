import requests

cookies = {
    'did': '9e9e9085-06c8-4b06-8591-19829cabe02e',
    'cdid': '0bebccea-177c-446e-a1ef-1d18005175fa',
    'city': 'maragheh',
    'theme': 'dark',
    'referrer': '',
    '_vid_t': 'fbocKQF+4cT1K4b2Ncp5A08Un7kMWKmtvzSOKTuCuA8R2cUHa1rDITwNWXOAVXF8fzb75VVhbkOiAA==',
    'multi-city': 'azarbaijan-east-province%7C',
    'csid': 'e9a0596d605524a7de',
    'sAccessToken': 'eyJraWQiOiJkLTE3ODM4NTM5ODA5NTEiLCJ0eXAiOiJKV1QiLCJ2ZXJzaW9uIjoiNCIsImFsZyI6IlJTMjU2In0.eyJpYXQiOjE3ODQ0NTA4OTYsImV4cCI6MTc4NDQ2MTY5Niwic3ViIjoiOWM5NjU0MDMtMzk2Yy00ZDI2LWIxY2UtOGM2ODVmYzNjNjkyIiwidElkIjoicHVibGljIiwic2Vzc2lvbkhhbmRsZSI6ImNkNTY3NjYxLTYzYjctNDc4ZS04MjAwLTE5ZWZiNTY4MTA3MSIsInJlZnJlc2hUb2tlbkhhc2gxIjoiZGI0Mzc1NTFmNTA0MjU3YmM0NmQyZGMzYTk2ZmM5MDJmMDBlNmQwYzBmY2QwNWVhOWNlY2FhMTM5YmVhNjFmMyIsInBhcmVudFJlZnJlc2hUb2tlbkhhc2gxIjoiYjVhMmNiZjc0MGM3YjkxMThmODJlMzRmNzA0Y2RlZTFlZmYxZDdhMWJlNTdmNDU3NTRlMDRiNDk3ZDE0YTNmZiIsImFudGlDc3JmVG9rZW4iOm51bGwsImlzcyI6Imh0dHBzOi8vYXBpLmRpdmFyLmlyL3Y4L2F1dGhlbnRpY2F0ZSIsInBob25lTnVtYmVyIjoiKzk4OTA0NDY2ODc4OCIsInN0LXBlcm0iOnsidCI6MTc4NDQ1MDg5NiwidiI6W119LCJzdC1yb2xlIjp7InQiOjE3ODQ0NTA4OTYsInYiOltdfX0.UB6pxWw2r3mzhTpCkJZRjjJU16XyIcnS240wELXcvmB4sJ-TKCHWKu6_3m8Sqc9aHC7Ag8exa_ZojJ5UIa0qrE0eI7AGVojrdlCCGowgh2v0EtQLc9eF6eRHvVFd3pLLtYSThZTCTdWwaERNELphQ4sNHugA4jxHtGVPMvMK-eExQfq6LFntITgPYx9Ni34rr38zpEkQBUhcZ_nmYUMhlpwf3mB8qNpL4_ep3oUzCqzmwoRn5dDbs8mo9mDOTQ3yi_xb_fY7cB9LvUuCZpqCxLS9_CMAy49bSWZ2PtmGrwjhSi4129yu6KSIah1WQhg9aN-Bw2UvZFDVO6xycu1S0w',
    'sFrontToken': 'eyJ1aWQiOiI5Yzk2NTQwMy0zOTZjLTRkMjYtYjFjZS04YzY4NWZjM2M2OTIiLCJhdGUiOjE3ODQ0NjE2OTYwMDAsInVwIjp7ImFudGlDc3JmVG9rZW4iOm51bGwsImV4cCI6MTc4NDQ2MTY5NiwiaWF0IjoxNzg0NDUwODk2LCJpc3MiOiJodHRwczovL2FwaS5kaXZhci5pci92OC9hdXRoZW50aWNhdGUiLCJwYXJlbnRSZWZyZXNoVG9rZW5IYXNoMSI6ImI1YTJjYmY3NDBjN2I5MTE4ZjgyZTM0ZjcwNGNkZWUxZWZmMWQ3YTFiZTU3ZjQ1NzU0ZTA0YjQ5N2QxNGEzZmYiLCJwaG9uZU51bWJlciI6Iis5ODkwNDQ2Njg3ODgiLCJyZWZyZXNoVG9rZW5IYXNoMSI6ImRiNDM3NTUxZjUwNDI1N2JjNDZkMmRjM2E5NmZjOTAyZjAwZTZkMGMwZmNkMDVlYTljZWNhYTEzOWJlYTYxZjMiLCJzZXNzaW9uSGFuZGxlIjoiY2Q1Njc2NjEtNjNiNy00NzhlLTgyMDAtMTllZmI1NjgxMDcxIiwic3QtcGVybSI6eyJ0IjoxNzg0NDUwODk2LCJ2IjpbXX0sInN0LXJvbGUiOnsidCI6MTc4NDQ1MDg5NiwidiI6W119LCJzdWIiOiI5Yzk2NTQwMy0zOTZjLTRkMjYtYjFjZS04YzY4NWZjM2M2OTIiLCJ0SWQiOiJwdWJsaWMifX0=',
    'ff': '%7B%22f%22%3A%7B%22foreigner_payment_enabled%22%3Atrue%2C%22enable_filter_post_count_web%22%3Atrue%2C%22device_fp_enable%22%3Atrue%2C%22enable-places-selector-online-search-web%22%3Atrue%2C%22chat_message_disabled%22%3Atrue%2C%22web_sentry_sample_rate%22%3A0.2%2C%22web_sentry_traces_sample_rate%22%3A0.01%2C%22is_web_proactive_refresh_enabled%22%3Atrue%2C%22post-stats-batch-event-web-max-batch-size%22%3A%2220%22%2C%22post-stats-batch-event-web-flush-interval-sec%22%3A%2220%22%7D%2C%22e%22%3A1784454496851%2C%22r%22%3A1784537296851%7D',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'baggage': 'sentry-environment=client,sentry-release=release-the-wall-matching-d74a1e04,sentry-public_key=7e7d19d51ebe4bd5955fda8ab50107b1,sentry-trace_id=aec167df31134eed65e658c99bc6599a,sentry-sampled=false,sentry-sample_rand=0.07707081783887537,sentry-sample_rate=0.01',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://divar.ir',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://divar.ir/',
    'sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="150", "Google Chrome";v="150"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sentry-trace': 'aec167df31134eed65e658c99bc6599a-f71ea3478781a360-0',
    'traceparent': '00-aec167df31134eed65e658c99bc6599a-f71ea3478781a360-00',
    'tracestate': 'sentry.sampled_not_recording=1,sentry.sample_rand=0.07707081783887537,sentry.sample_rate=0.01,sentry.url=https://api.divar.ir/v8/postlist/w/search',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36',
    'x-render-type': 'CSR',
    'x-screen-size': '1060x731',
    'x-standard-divar-error': 'true',
    # 'cookie': 'did=9e9e9085-06c8-4b06-8591-19829cabe02e; cdid=0bebccea-177c-446e-a1ef-1d18005175fa; city=maragheh; theme=dark; referrer=; _vid_t=fbocKQF+4cT1K4b2Ncp5A08Un7kMWKmtvzSOKTuCuA8R2cUHa1rDITwNWXOAVXF8fzb75VVhbkOiAA==; multi-city=azarbaijan-east-province%7C; csid=e9a0596d605524a7de; sAccessToken=eyJraWQiOiJkLTE3ODM4NTM5ODA5NTEiLCJ0eXAiOiJKV1QiLCJ2ZXJzaW9uIjoiNCIsImFsZyI6IlJTMjU2In0.eyJpYXQiOjE3ODQ0NTA4OTYsImV4cCI6MTc4NDQ2MTY5Niwic3ViIjoiOWM5NjU0MDMtMzk2Yy00ZDI2LWIxY2UtOGM2ODVmYzNjNjkyIiwidElkIjoicHVibGljIiwic2Vzc2lvbkhhbmRsZSI6ImNkNTY3NjYxLTYzYjctNDc4ZS04MjAwLTE5ZWZiNTY4MTA3MSIsInJlZnJlc2hUb2tlbkhhc2gxIjoiZGI0Mzc1NTFmNTA0MjU3YmM0NmQyZGMzYTk2ZmM5MDJmMDBlNmQwYzBmY2QwNWVhOWNlY2FhMTM5YmVhNjFmMyIsInBhcmVudFJlZnJlc2hUb2tlbkhhc2gxIjoiYjVhMmNiZjc0MGM3YjkxMThmODJlMzRmNzA0Y2RlZTFlZmYxZDdhMWJlNTdmNDU3NTRlMDRiNDk3ZDE0YTNmZiIsImFudGlDc3JmVG9rZW4iOm51bGwsImlzcyI6Imh0dHBzOi8vYXBpLmRpdmFyLmlyL3Y4L2F1dGhlbnRpY2F0ZSIsInBob25lTnVtYmVyIjoiKzk4OTA0NDY2ODc4OCIsInN0LXBlcm0iOnsidCI6MTc4NDQ1MDg5NiwidiI6W119LCJzdC1yb2xlIjp7InQiOjE3ODQ0NTA4OTYsInYiOltdfX0.UB6pxWw2r3mzhTpCkJZRjjJU16XyIcnS240wELXcvmB4sJ-TKCHWKu6_3m8Sqc9aHC7Ag8exa_ZojJ5UIa0qrE0eI7AGVojrdlCCGowgh2v0EtQLc9eF6eRHvVFd3pLLtYSThZTCTdWwaERNELphQ4sNHugA4jxHtGVPMvMK-eExQfq6LFntITgPYx9Ni34rr38zpEkQBUhcZ_nmYUMhlpwf3mB8qNpL4_ep3oUzCqzmwoRn5dDbs8mo9mDOTQ3yi_xb_fY7cB9LvUuCZpqCxLS9_CMAy49bSWZ2PtmGrwjhSi4129yu6KSIah1WQhg9aN-Bw2UvZFDVO6xycu1S0w; sFrontToken=eyJ1aWQiOiI5Yzk2NTQwMy0zOTZjLTRkMjYtYjFjZS04YzY4NWZjM2M2OTIiLCJhdGUiOjE3ODQ0NjE2OTYwMDAsInVwIjp7ImFudGlDc3JmVG9rZW4iOm51bGwsImV4cCI6MTc4NDQ2MTY5NiwiaWF0IjoxNzg0NDUwODk2LCJpc3MiOiJodHRwczovL2FwaS5kaXZhci5pci92OC9hdXRoZW50aWNhdGUiLCJwYXJlbnRSZWZyZXNoVG9rZW5IYXNoMSI6ImI1YTJjYmY3NDBjN2I5MTE4ZjgyZTM0ZjcwNGNkZWUxZWZmMWQ3YTFiZTU3ZjQ1NzU0ZTA0YjQ5N2QxNGEzZmYiLCJwaG9uZU51bWJlciI6Iis5ODkwNDQ2Njg3ODgiLCJyZWZyZXNoVG9rZW5IYXNoMSI6ImRiNDM3NTUxZjUwNDI1N2JjNDZkMmRjM2E5NmZjOTAyZjAwZTZkMGMwZmNkMDVlYTljZWNhYTEzOWJlYTYxZjMiLCJzZXNzaW9uSGFuZGxlIjoiY2Q1Njc2NjEtNjNiNy00NzhlLTgyMDAtMTllZmI1NjgxMDcxIiwic3QtcGVybSI6eyJ0IjoxNzg0NDUwODk2LCJ2IjpbXX0sInN0LXJvbGUiOnsidCI6MTc4NDQ1MDg5NiwidiI6W119LCJzdWIiOiI5Yzk2NTQwMy0zOTZjLTRkMjYtYjFjZS04YzY4NWZjM2M2OTIiLCJ0SWQiOiJwdWJsaWMifX0=; ff=%7B%22f%22%3A%7B%22foreigner_payment_enabled%22%3Atrue%2C%22enable_filter_post_count_web%22%3Atrue%2C%22device_fp_enable%22%3Atrue%2C%22enable-places-selector-online-search-web%22%3Atrue%2C%22chat_message_disabled%22%3Atrue%2C%22web_sentry_sample_rate%22%3A0.2%2C%22web_sentry_traces_sample_rate%22%3A0.01%2C%22is_web_proactive_refresh_enabled%22%3Atrue%2C%22post-stats-batch-event-web-max-batch-size%22%3A%2220%22%2C%22post-stats-batch-event-web-flush-interval-sec%22%3A%2220%22%7D%2C%22e%22%3A1784454496851%2C%22r%22%3A1784537296851%7D',
}

json_data = {
    'city_ids': [
        '891',
    ],
    'pagination_data': {
        '@type': 'type.googleapis.com/post_list.PaginationData',
        'last_post_date': '2026-07-19T08:47:08.824414Z',
        'page': 1,
        'layer_page':1,
        'search_uid': '69f8314f-4e05-4a40-aa29-c3ae2946b09a',
        'cumulative_widgets_count': 48,
        'viewed_tokens': 'H4sIAAAAAAAE/zTQUW+bMBDA8S90lUpmr/FjDIS6UMCwpnJe0I0mziCLQSRL2KefzmhvP/3vECdbbIXZxkew2PLEjBFBqKIIwO5dyLBzvjhtvhG4ebk3C+ZdDRbNebCHPRWhyp5QfzzlY7WUHE8eLi+MBwuLC1iseLk7T1Su7Jejn+pBqV1CRbhs/g0Wu/6rW71Q4axJ1mDx536c1zFY/HwEfXKjkXDpTYHGrr9/dH9oRzApCa0wb/wZLL4/3usJQWP6Gshm5b9S26NdoLINgTvx/9Qo41QEi0JNCFR2TQlc8WJ5KLYSDyrCReUGNE7D06mUvqiIMQ8W1SHdM8Qy+QEaX9Muln/B4uieq3SCDbpbY64Hv+zk53cPE+YdaLxE4VzRaHtff+k3sNgKJwv3LwAA//+7KT/DrwEAAA==',
        'search_bookmark_info': {
            'search_hash': '1551f29557706dbbe16ac2ab9f796ffe',
            'bookmark_state': {},
            'alert_state': {},
        },
        'first_page_viewed_at': '2026-07-19T08:48:16.953281171Z',
    },
    'disable_recommendation': False,
    'map_state': {
        'camera_info': {
            'bbox': {},
        },
    },
    'search_data': {
        'form_data': {
            'data': {
                'category': {
                    'str': {
                        'value': 'ROOT',
                    },
                },
            },
        },
        'server_payload': {
            '@type': 'type.googleapis.com/widgets.SearchData.ServerPayload',
            'additional_form_data': {
                'data': {
                    'sort': {
                        'str': {
                            'value': 'sort_date',
                        },
                    },
                },
            },
        },
    },
}

response = requests.post('https://api.divar.ir/v8/postlist/w/search', cookies=cookies, headers=headers, json=json_data)
print(response.text)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"city_ids":["891"],"pagination_data":{"@type":"type.googleapis.com/post_list.PaginationData","last_post_date":"2026-07-19T08:47:08.824414Z","page":2,"layer_page":2,"search_uid":"69f8314f-4e05-4a40-aa29-c3ae2946b09a","cumulative_widgets_count":48,"viewed_tokens":"H4sIAAAAAAAE/zTQUW+bMBDA8S90lUpmr/FjDIS6UMCwpnJe0I0mziCLQSRL2KefzmhvP/3vECdbbIXZxkew2PLEjBFBqKIIwO5dyLBzvjhtvhG4ebk3C+ZdDRbNebCHPRWhyp5QfzzlY7WUHE8eLi+MBwuLC1iseLk7T1Su7Jejn+pBqV1CRbhs/g0Wu/6rW71Q4axJ1mDx536c1zFY/HwEfXKjkXDpTYHGrr9/dH9oRzApCa0wb/wZLL4/3usJQWP6Gshm5b9S26NdoLINgTvx/9Qo41QEi0JNCFR2TQlc8WJ5KLYSDyrCReUGNE7D06mUvqiIMQ8W1SHdM8Qy+QEaX9Muln/B4uieq3SCDbpbY64Hv+zk53cPE+YdaLxE4VzRaHtff+k3sNgKJwv3LwAA//+7KT/DrwEAAA==","search_bookmark_info":{"search_hash":"1551f29557706dbbe16ac2ab9f796ffe","bookmark_state":{},"alert_state":{}},"first_page_viewed_at":"2026-07-19T08:48:16.953281171Z"},"disable_recommendation":false,"map_state":{"camera_info":{"bbox":{}}},"search_data":{"form_data":{"data":{"category":{"str":{"value":"ROOT"}}}},"server_payload":{"@type":"type.googleapis.com/widgets.SearchData.ServerPayload","additional_form_data":{"data":{"sort":{"str":{"value":"sort_date"}}}}}}}'
#response = requests.post('https://api.divar.ir/v8/postlist/w/search', cookies=cookies, headers=headers, data=data)