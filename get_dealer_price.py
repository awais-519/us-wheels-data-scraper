import requests, json

def dealer_prices(product_list):
    cookies = {
        'apex__effacc': '0016Q00001vUWmGQAW',
        'CookieConsentPolicy': '0:1',
        'LSKey-c$CookieConsentPolicy': '0:1',
        'BrowserId': 'cF68cU_REe6UFKl-_BXbww',
        'BrowserId_sec': 'cF68cU_REe6UFKl-_BXbww',
        '_ga': 'GA1.2.1517644002.1694347148',
        '_gid': 'GA1.2.1622944415.1694347148',
        'pctrk': 'b99ee54b-09ea-4a66-9c9b-f08506785cb9',
        'oinfo': 'c3RhdHVzPUFDVElWRSZ0eXBlPTImb2lkPTAwRDFVMDAwMDAweThLNg==',
        'autocomplete': '1',
        'oid': '00D1U000000y8K6',
        'ak_bmsc': '527B76EE4A41C15A12478CCB331EAECF~000000000000000000000000000000~YAAQDrOvw8e8ekSKAQAA7PSyhRVm5HQrZ+Ysui55b7sEtDBe4SLGOq2ih+Pa6A/8YGFRjiVUkhZsNgAdyfN5IDpxcbCdQz49nkDOgUr/ravkYpBVaq270PdBQovaYwLhpcarEiNoUCpurVoLiVXHLHeomnusXkOF2poE2j89hJRV4WinsNgyUgc/casJ62vs8QOutPCCs3TmZzmDF6Ez/h6pnXpyzpFACiHJrfIXp4OIi19zn05+slC8l7Q5Z6gNGv91ch8ouD4pQ3AR2TBClkG7KyyDfQw8YxVxqAYpU5NqCHROS2jixOUMvAV/crpK9JOkqrJQFiZPf4cgic8f2V4tTxZIp0u2otLQiFipEeiLYn6RKG4Cx9KtrADFlwWNJ2/CC9+L8gjjDqM=',
        'apex__cclgtkn': '',
        'apex__cc_anonymous_Currency': 'TRY',
        'apex__cc_anonymous_Country': 'TR',
        '__kla_id': 'eyIkcmVmZXJyZXIiOnsidHMiOjE2OTQzNDcxNTAsInZhbHVlIjoiaHR0cHM6Ly93aGVlbHByb3MubXkuc2l0ZS5jb20vZGVhbGVybGluZS9hcGV4L2NjcnpfX2hvbWVwYWdlP3N0b3JlPWRlYWxlcmxpbmUiLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93aGVlbHByb3MubXkuc2l0ZS5jb20vZGVhbGVybGluZS9jY3J6X19DQ1NpdGVMb2dpbiJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTY5NDQ2MDIxNCwidmFsdWUiOiIiLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93aGVlbHByb3MubXkuc2l0ZS5jb20vZGVhbGVybGluZS9jY3J6X19DQ1NpdGVMb2dpbj9zdGFydFVSTD0lMkZkZWFsZXJsaW5lJTJGYWxsLXByb2R1Y3RzJTNGdmlld1N0YXRlJTNETGlzdFZpZXclMjZjYXJ0SUQlM0RkZjFjMjFmMC1kODhhLTRkOTItYmExZi1hNTZhOGU0ZmU4MjklMjZwb3J0YWxVc2VyJTNEJTI2c3RvcmUlM0RkZWFsZXJsaW5lJTI2ZWZmZWN0aXZlQWNjb3VudCUzRDAwMTZRMDAwMDF2VVdtR1FBVyUyNmNjbGNsJTNEZW5fVVMifX0=',
        'sid': '00D1U000000y8K6!AQQAQInZKf16yIouKYmV8WBLgjADu3mD0jn8xDxq6LC03lPdgrmn1O0tNo8y2TSCzzj3XcOMQiLp5yqC2cRSGL1BSUP5Q6Zm',
        'sid_Client': 'Q00000ABWbVU000000y8K6',
        'clientSrc': '37.130.93.120',
        'inst': 'APP_6Q',
        '_gat_dealerline': '1',
        '_ga_5PD1VH042R': 'GS1.2.1694463846.13.1.1694463966.60.0.0',
        'bm_sv': 'B1E53BF07497FC9A338876C2E2CD5C89~YAAQnrGvw+t6M0SKAQAA13HshRWjud7JBHNx6R9zE3vDe9Naby1QtPWX2mh2dRsNfARSBgmZ/UUL4IeEjXF6YHU3HV/gIsBqT9jf5PolrXXg/oiRvmcsX6l6g/MuRyx8JoHvSEV40ygXjlAlPFV2Wtonk0Ez5cq2iCa5KpNTzdAfOmonJUrPvIzalVaOa5nUvefCKPClMAzlp7KJvGmB/ydkQfqSS4EKO9G7g2Kn6AlU7KOJw0K2+jYmPwocl4xK8Cs=~1',
    }

    headers = {
        'authority': 'wheelpros.my.site.com',
        'accept': '*/*',
        'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        # 'cookie': 'apex__effacc=0016Q00001vUWmGQAW; CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1; BrowserId=cF68cU_REe6UFKl-_BXbww; BrowserId_sec=cF68cU_REe6UFKl-_BXbww; _ga=GA1.2.1517644002.1694347148; _gid=GA1.2.1622944415.1694347148; pctrk=b99ee54b-09ea-4a66-9c9b-f08506785cb9; oinfo=c3RhdHVzPUFDVElWRSZ0eXBlPTImb2lkPTAwRDFVMDAwMDAweThLNg==; autocomplete=1; oid=00D1U000000y8K6; ak_bmsc=527B76EE4A41C15A12478CCB331EAECF~000000000000000000000000000000~YAAQDrOvw8e8ekSKAQAA7PSyhRVm5HQrZ+Ysui55b7sEtDBe4SLGOq2ih+Pa6A/8YGFRjiVUkhZsNgAdyfN5IDpxcbCdQz49nkDOgUr/ravkYpBVaq270PdBQovaYwLhpcarEiNoUCpurVoLiVXHLHeomnusXkOF2poE2j89hJRV4WinsNgyUgc/casJ62vs8QOutPCCs3TmZzmDF6Ez/h6pnXpyzpFACiHJrfIXp4OIi19zn05+slC8l7Q5Z6gNGv91ch8ouD4pQ3AR2TBClkG7KyyDfQw8YxVxqAYpU5NqCHROS2jixOUMvAV/crpK9JOkqrJQFiZPf4cgic8f2V4tTxZIp0u2otLQiFipEeiLYn6RKG4Cx9KtrADFlwWNJ2/CC9+L8gjjDqM=; apex__cclgtkn=; apex__cc_anonymous_Currency=TRY; apex__cc_anonymous_Country=TR; __kla_id=eyIkcmVmZXJyZXIiOnsidHMiOjE2OTQzNDcxNTAsInZhbHVlIjoiaHR0cHM6Ly93aGVlbHByb3MubXkuc2l0ZS5jb20vZGVhbGVybGluZS9hcGV4L2NjcnpfX2hvbWVwYWdlP3N0b3JlPWRlYWxlcmxpbmUiLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93aGVlbHByb3MubXkuc2l0ZS5jb20vZGVhbGVybGluZS9jY3J6X19DQ1NpdGVMb2dpbiJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTY5NDQ2MDIxNCwidmFsdWUiOiIiLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93aGVlbHByb3MubXkuc2l0ZS5jb20vZGVhbGVybGluZS9jY3J6X19DQ1NpdGVMb2dpbj9zdGFydFVSTD0lMkZkZWFsZXJsaW5lJTJGYWxsLXByb2R1Y3RzJTNGdmlld1N0YXRlJTNETGlzdFZpZXclMjZjYXJ0SUQlM0RkZjFjMjFmMC1kODhhLTRkOTItYmExZi1hNTZhOGU0ZmU4MjklMjZwb3J0YWxVc2VyJTNEJTI2c3RvcmUlM0RkZWFsZXJsaW5lJTI2ZWZmZWN0aXZlQWNjb3VudCUzRDAwMTZRMDAwMDF2VVdtR1FBVyUyNmNjbGNsJTNEZW5fVVMifX0=; sid=00D1U000000y8K6!AQQAQInZKf16yIouKYmV8WBLgjADu3mD0jn8xDxq6LC03lPdgrmn1O0tNo8y2TSCzzj3XcOMQiLp5yqC2cRSGL1BSUP5Q6Zm; sid_Client=Q00000ABWbVU000000y8K6; clientSrc=37.130.93.120; inst=APP_6Q; _gat_dealerline=1; _ga_5PD1VH042R=GS1.2.1694463846.13.1.1694463966.60.0.0; bm_sv=B1E53BF07497FC9A338876C2E2CD5C89~YAAQnrGvw+t6M0SKAQAA13HshRWjud7JBHNx6R9zE3vDe9Naby1QtPWX2mh2dRsNfARSBgmZ/UUL4IeEjXF6YHU3HV/gIsBqT9jf5PolrXXg/oiRvmcsX6l6g/MuRyx8JoHvSEV40ygXjlAlPFV2Wtonk0Ez5cq2iCa5KpNTzdAfOmonJUrPvIzalVaOa5nUvefCKPClMAzlp7KJvGmB/ydkQfqSS4EKO9G7g2Kn6AlU7KOJw0K2+jYmPwocl4xK8Cs=~1',
        'origin': 'https://wheelpros.my.site.com',
        'referer': 'https://wheelpros.my.site.com/dealerline/all-products?viewState=ListView&cartID=df1c21f0-d88a-4d92-ba1f-a56a8e4fe829&portalUser=&store=dealerline&effectiveAccount=0016Q00001vUWmGQAW&cclcl=en_US',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-user-agent': 'Visualforce-Remoting',
    }

    json_data = {
        'action': 'AppGuideController',
        'method': 'getFormulasBasedOnName',
        'data': [
            {
                'storefront': 'dealerline',
                'portalUserId': '',
                'effAccountId': '0016Q00001vUWmGQAW',
                'priceGroupId': '',
                'currentCartId': 'df1c21f0-d88a-4d92-ba1f-a56a8e4fe829',
                'userIsoCode': 'USD',
                'userLocale': 'en_US',
                'currentPageName': 'ccrz__ProductList',
                'currentPageURL': 'https://wheelpros.my.site.com/dealerline/ccrz__ProductList?cartID=df1c21f0-d88a-4d92-ba1f-a56a8e4fe829&categoryId=a0K1U000005ip3CUAQ&cclcl=en_US&effectiveAccount=0016Q00001vUWmGQAW&portalUser=&store=dealerline&viewState=ListView&refURL=https%3A%2F%2Fwheelpros.my.site.com%2Fdealerline%2Fapex%2Fccrz__homepage%3Fstore%3Ddealerline',
                'queryParams': {
                    'viewState': 'ListView',
                    'cartID': 'df1c21f0-d88a-4d92-ba1f-a56a8e4fe829',
                    'portalUser': '',
                    'store': 'dealerline',
                    'effectiveAccount': '0016Q00001vUWmGQAW',
                    'cclcl': 'en_US',
                },
            },
            product_list,
        ],
        'type': 'rpc',
        'tid': 23,
        'ctx': {
            'csrf': 'VmpFPSxNakF5TXkwd09TMHlNRlF4TWpvek1qb3pPUzQzTkRaYSxGZ21fUmFnUG9hczVJTmRwdno1RGc4czBzVDBGbTI2REJ4Zmt3RHlFWF9rPSxNVEUyT0dFdw==',
            'vid': '0661U000005ihTF',
            'ns': '',
            'ver': 45,
            'authorization': 'eyJub25jZSI6IlFvMlYxVy05bHY1WUxIaDFSNVBsQVd5c0lLYy03ckdjZm5GdmFpOG9VWndcdTAwM2QiLCJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IntcInRcIjpcIjAwRDFVMDAwMDAweThLNlwiLFwidlwiOlwiMDJHMVUwMDAwMDBjdktCXCIsXCJhXCI6XCJ2ZnJlbW90aW5nc2lnbmluZ2tleVwiLFwidVwiOlwiMDA1NlEwMDAwMEFCV2JWXCJ9IiwiY3JpdCI6WyJpYXQiXSwiaWF0IjoxNjk0OTUzOTU5NzQ2LCJleHAiOjB9.Q2lsQmNIQkhkV2xrWlVOdmJuUnliMnhzWlhJdVoyVjBSbTl5YlhWc1lYTkNZWE5sWkU5dVRtRnRaUT09.IwMqEDg30xN1I1-Wk-VADf9ikH8blm_FFjaGbUbul4Q=',
        },
    }

    response = requests.post('https://wheelpros.my.site.com/dealerline/apexremote',  headers=headers, json=json_data)
    
    json.loads(response.text)
    if response.status_code != 200:
        print("Not OK")
    print(response.text)
    return response


# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"action":"AppGuideController","method":"getFormulasBasedOnName","data":[{"storefront":"dealerline","portalUserId":"","effAccountId":"0016Q00001vUWmGQAW","priceGroupId":"","currentCartId":"df1c21f0-d88a-4d92-ba1f-a56a8e4fe829","userIsoCode":"USD","userLocale":"en_US","currentPageName":"ccrz__ProductList","currentPageURL":"https://wheelpros.my.site.com/dealerline/ccrz__ProductList?cartID=df1c21f0-d88a-4d92-ba1f-a56a8e4fe829&categoryId=a0K1U000005ip3CUAQ&cclcl=en_US&effectiveAccount=0016Q00001vUWmGQAW&portalUser=&store=dealerline&viewState=ListView&refURL=https%3A%2F%2Fwheelpros.my.site.com%2Fdealerline%2Fsecur%2Ffrontdoor.jsp%3Fallp%3D1%26apv%3D1%26cshc%3DQ00000ABWbVU000000y8K6%26refURL%3Dhttps%253A%252F%252Fwheelpros.my.site.com%252Fdealerline%252Fsecur%252Ffrontdoor.jsp%26retURL%3D%252Fdealerline%252Fall-products%253FviewState%253DListView%2526cartID%253Ddf1c21f0-d88a-4d92-ba1f-a56a8e4fe829%2526portalUser%253D%2526store%253Ddealerline%2526effectiveAccount%253D0016Q00001vUWmGQAW%2526cclcl%253Den_US%26sid%3D00D1U000000y8K6%2521AQQAQHfyoPFn1ubuDsKIIol4M__DLBMyr.LfDDWO2KHN.QyYQAvBo51uJjtL6FOY7aZjSlDPkcOAEkDmCub3Ii4uQ6opFC50%26untethered%3D","queryParams":{"viewState":"ListView","cartID":"df1c21f0-d88a-4d92-ba1f-a56a8e4fe829","portalUser":"","store":"dealerline","effectiveAccount":"0016Q00001vUWmGQAW","cclcl":"en_US"}},"[{\\"sku\\":\\"U415190090+4035\\",\\"category\\":\\"Wheels\\",\\"randomString\\":\\"\\"},{\\"sku\\":\\"H880192062+4135\\",\\"category\\":\\"Wheels\\",\\"randomString\\":\\"GWJ611\\"},{\\"sku\\":\\"F23719906150\\",\\"category\\":\\"Wheels\\",\\"randomString\\":\\"\\"},{\\"sku\\":\\"U587208061+01T\\",\\"category\\":\\"Wheels\\",\\"randomString\\":\\"\\"},{\\"sku\\":\\"U331208061+01TL\\",\\"category\\":\\"Wheels\\",\\"randomString\\":\\"pjx617\\"},{\\"sku\\":\\"U587220561+01T\\",\\"category\\":\\"Wheels\\",\\"randomString\\":\\"\\"},{\\"sku\\":\\"U313220561+01TL\\",\\"category\\":\\"Wheels\\",\\"randomString\\":\\"\\"},{\\"sku\\":\\"U313220561+01TR\\",\\"category\\":\\"Wheels\\",\\"randomString\\":\\"\\"},{\\"sku\\":\\"U524220577+01TR\\",\\"category\\":\\"Wheels\\",\\"randomString\\":\\"\\"},{\\"sku\\":\\"U524220577+01TL\\",\\"category\\":\\"Wheels\\",\\"randomString\\":\\"\\"},{\\"sku\\":\\"U313228561+07TL\\",\\"category\\":\\"Wheels\\",\\"randomString\\":\\"\\"},{\\"sku\\":\\"U313228561+07TR\\",\\"category\\":\\"Wheels\\",\\"randomString\\":\\"\\"},{\\"sku\\":\\"U524228577+07TR\\",\\"category\\":\\"Wheels\\",\\"randomString\\":\\"\\"},{\\"sku\\":\\"U3652490B4+25TL\\",\\"category\\":\\"Wheels\\",\\"randomString\\":\\"\\"},{\\"sku\\":\\"AF142-19853035BKA1\\",\\"category\\":\\"Wheels\\",\\"randomString\\":\\"\\"},{\\"sku\\":\\"AF142-19953014BKA1\\",\\"category\\":\\"Wheels\\",\\"randomString\\":\\"\\"},{\\"sku\\":\\"AF173-22105630BRA1\\",\\"category\\":\\"Wheels\\",\\"randomString\\":\\"\\"},{\\"sku\\":\\"AF173-22905624BRA1\\",\\"category\\":\\"Wheels\\",\\"randomString\\":\\"\\"},{\\"sku\\":\\"AF174-22105630BKA1\\",\\"category\\":\\"Wheels\\",\\"randomString\\":\\"\\"},{\\"sku\\":\\"AF174-22905624BKA1\\",\\"category\\":\\"Wheels\\",\\"randomString\\":\\"\\"},{\\"sku\\":\\"AF832-26105004GLA1\\",\\"category\\":\\"Wheels\\",\\"randomString\\":\\"\\"},{\\"sku\\":\\"AF832-26905006GLA1\\",\\"category\\":\\"Wheels\\",\\"randomString\\":\\"\\"},{\\"sku\\":\\"AF841-2410346NBRLF\\",\\"category\\":\\"Wheels\\",\\"randomString\\":\\"\\"},{\\"sku\\":\\"AF841-2410346NBRRT\\",\\"category\\":\\"Wheels\\",\\"randomString\\":\\"\\"},{\\"sku\\":\\"AF841-24903405BRLF\\",\\"category\\":\\"Wheels\\",\\"randomString\\":\\"\\"}]"],"type":"rpc","tid":21,"ctx":{"csrf":"VmpFPSxNakF5TXkwd09TMHhORlF5TURveU5qb3dOaTR5TXpSYSxWRXpvSTZ4RkhQYUEtVFZ1RzhZZk5KRGo1M25lRlZIT3doNHBnMHNwOUE4PSxNVEUyT0dFdw==","vid":"0661U000005ihTF","ns":"","ver":45,"authorization":"eyJub25jZSI6ImhoRlUxQl9GRHhsdF8zRkVtQWh6eTV2SG1KcmVYOFpWb0pmVnJqRmR6RnNcdTAwM2QiLCJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IntcInRcIjpcIjAwRDFVMDAwMDAweThLNlwiLFwidlwiOlwiMDJHMVUwMDAwMDBjdktCXCIsXCJhXCI6XCJ2ZnJlbW90aW5nc2lnbmluZ2tleVwiLFwidVwiOlwiMDA1NlEwMDAwMEFCV2JWXCJ9IiwiY3JpdCI6WyJpYXQiXSwiaWF0IjoxNjk0NDYzOTY2MjM1LCJleHAiOjB9.Q2lsQmNIQkhkV2xrWlVOdmJuUnliMnhzWlhJdVoyVjBSbTl5YlhWc1lYTkNZWE5sWkU5dVRtRnRaUT09.EoNEQZK7PhnInuEmylfea8jekdM3PQAzMyS5ekdAYEM="}}'
#response = requests.post('https://wheelpros.my.site.com/dealerline/apexremote', cookies=cookies, headers=headers, data=data)