import pytest
import requests
import logging
import json

"""
全局仅登录一次，获取token，
在请求头部添加Authentication Bearer 认证
内置fixture requests_session
"""


@pytest.fixture(scope="session", autouse=True)
def login(requests_session):
    """登录方法"""
    # 调用登录方法，返回token
    cookies = {
        'Cookie': 'HttpOnly; vk=757e2e1b-9718-4114-bf73-5b468bfe795c; deviceid=uZ368qDi; cbc-sid=204936ee373e7d543ace717b45fb95d07bfbc31a07328590f3a398d808a5f3185b5ba0a7377e375137b8; recentServices=["workplace"]; siteCode=2B32DC97D4D74484816EB181BE7C67A3; siteThirdLoginUrl=undefined; siteType=1; siteThirdAuthType=undefined; siteTenantId=undefined; ua=admin@d16fa496f47; lang=zh; TWO-FACTOR-LOGIN-CODE="A5Dgngl+jV9vD6CFXPjOfg==WqeQcQyw+yRjrj4GcetNPLq25fNvMk99O88Gx47MV68GfpD11+PR4exPgJO0MNjPpHmIy6idXFNU3gB8ggfInUc="; HWWAFSESID=5412979515d17d4088; HWWAFSESTIME=1682835657599; cdn_token=A732A9AEE6984CFA97D9313C2A2E99A9#1682878868#6a1d553d578b6a3a0a259d070917f3d546a46d0369c7301894d22f897ebba0fc; x-wlk-gray=0; SessionID=1814c1c8-bccc-49bf-bf46-88ab28d24054; ad_sc=; ad_mdm=; ad_cmp=; ad_ctt=; ad_tm=; ad_adp=; cf=Direct; devclouddevuibjJ_SESSION_ID=66d80cc6e42a051f201acbd288b6f698c25e0644f8b03317; devclouddevuibjcftk=1F3X-ZJ0Z-COLX-SZB2-ZFJA-RSZ9-8PRT-6AUW; X-XSRF-TOKEN=3BBC237383C51D1165903ACB9D43050374DC292C04CE2F525AABFB1602FF54603C43524F69463EE43750F2F273D37E32DECE; JSESSIONID=A0A540D596F4594673297C5A01D4AF49F946368E17EE0BA9'}
    data = {
        'tenantId': 'A732A9AEE6984CFA97D9313C2A2E99A9',
        'thirdAuthType': 1,
        'userName': 'admin@d16fa496f47',
        'password': 'lkjLKJ+2023',
        'redirect_url': 'redirect_uri=https%3A%2F%2Fwelink.huaweicloud.com%2Fweb%2Fapp%2F%23%2Fathena-tenant%2FrightManaulTrigger%2FdesPage',
        'errorCode': None,
        'sliderUid': None,
        'mobile': '+86-18576797850'
    }
    res = requests_session.send_request(
        method='post',
        url='https://login.welink.huaweicloud.com/sso/v3/pclogintenant',
        data=data,
        cookies=cookies
    )
    header = res.headers
    token = header['X-XSRF-TOKEN']
    logging.info(f'---------token:{token}')
    logging.info(f'---------respose:{respose}')
    headers = {
        "X-XSRF-TOKEN": f"{token}"
    }
    requests_session.headers.update(headers)
