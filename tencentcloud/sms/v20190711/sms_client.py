# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.sms.v20190711 import models


class SmsClient(AbstractClient):
    _apiVersion = '2019-07-11'
    _endpoint = 'sms.tencentcloudapi.com'


    def AddSmsSign(self, request):
        """添加短信签名，申请之前请先认证参阅 [腾讯云短信签名审核标准](https://cloud.tencent.com/document/product/382/39022)。
        >⚠️注意：个人认证用户不支持使用 API 申请短信签名，请参阅了解 [实名认证基本介绍](https://cloud.tencent.com/document/product/378/3629)，如果为个人认证请登录控制台申请短信签名，具体操作请参阅 [创建短信签名](https://cloud.tencent.com/document/product/382/36136#Sign)。

        :param request: Request instance for AddSmsSign.
        :type request: :class:`tencentcloud.sms.v20190711.models.AddSmsSignRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.AddSmsSignResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddSmsSign", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddSmsSignResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddSmsTemplate(self, request):
        """添加短信模版，申请之前请先认证参阅 [腾讯云短信正文模版审核标准](https://cloud.tencent.com/document/product/382/39023)。
        >⚠️注意：个人认证用户不支持使用 API 申请短信正文模版，请参阅了解 [实名认证基本介绍](https://cloud.tencent.com/document/product/378/3629)，如果为个人认证请登录控制台申请短信正文模版，具体操作请参阅 [创建短信正文模版](https://cloud.tencent.com/document/product/382/36136#Template)。

        :param request: Request instance for AddSmsTemplate.
        :type request: :class:`tencentcloud.sms.v20190711.models.AddSmsTemplateRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.AddSmsTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddSmsTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddSmsTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CallbackStatusStatistics(self, request):
        """统计用户回执的数据。

        :param request: Request instance for CallbackStatusStatistics.
        :type request: :class:`tencentcloud.sms.v20190711.models.CallbackStatusStatisticsRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.CallbackStatusStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CallbackStatusStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CallbackStatusStatisticsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSmsSign(self, request):
        """>⚠️注意：个人认证用户不支持使用 API 删除短信签名，请参阅了解 [实名认证基本介绍](https://cloud.tencent.com/document/product/378/3629)，请登录控制台删除短信签名，具体操作请参阅 [短信签名操作](https://cloud.tencent.com/document/product/382/36136#Sign) 中查看删除短信签名须知。

        :param request: Request instance for DeleteSmsSign.
        :type request: :class:`tencentcloud.sms.v20190711.models.DeleteSmsSignRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.DeleteSmsSignResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSmsSign", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSmsSignResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSmsTemplate(self, request):
        """>⚠️注意：个人认证用户不支持使用 API 删除短信正文模版，请参阅了解 [实名认证基本介绍](https://cloud.tencent.com/document/product/378/3629)，请登录控制台删除短信正文模版，具体操作请参阅 [短信正文模版操作](https://cloud.tencent.com/document/product/382/36136#Template) 中查看删除短信正文模版须知。

        :param request: Request instance for DeleteSmsTemplate.
        :type request: :class:`tencentcloud.sms.v20190711.models.DeleteSmsTemplateRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.DeleteSmsTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSmsTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSmsTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSmsSignList(self, request):
        """>⚠️注意：个人认证用户不支持使用 API 查询短信签名，请参阅了解 [实名认证基本介绍](https://cloud.tencent.com/document/product/378/3629)。

        :param request: Request instance for DescribeSmsSignList.
        :type request: :class:`tencentcloud.sms.v20190711.models.DescribeSmsSignListRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.DescribeSmsSignListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSmsSignList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSmsSignListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSmsTemplateList(self, request):
        """>⚠️注意：个人认证用户不支持使用 API 查询短信正文模版，请参阅了解 [实名认证基本介绍](https://cloud.tencent.com/document/product/378/3629)。

        :param request: Request instance for DescribeSmsTemplateList.
        :type request: :class:`tencentcloud.sms.v20190711.models.DescribeSmsTemplateListRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.DescribeSmsTemplateListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSmsTemplateList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSmsTemplateListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySmsSign(self, request):
        """修改短信签名，修改之前请先认证参阅 [腾讯云短信签名审核标准](https://cloud.tencent.com/document/product/382/39022)。
        >- ⚠️注意：个人认证用户不支持使用 API 修改短信签名，请参阅了解 [实名认证基本介绍](https://cloud.tencent.com/document/product/378/3629)，如果为个人认证请登录控制台修改短信签名。
        >- 修改短信签名，仅当签名为待审核或已拒绝状态时，才能进行修改，已审核通过的签名不支持修改。

        :param request: Request instance for ModifySmsSign.
        :type request: :class:`tencentcloud.sms.v20190711.models.ModifySmsSignRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.ModifySmsSignResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySmsSign", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySmsSignResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySmsTemplate(self, request):
        """修改短信正文模版，修改之前请先认真参阅 [腾讯云短信正文模版审核标准](https://cloud.tencent.com/document/product/382/39023)。
        >- ⚠️注意：个人认证用户不支持使用 API 修改短信正文模版，请参阅了解 [实名认证基本介绍](https://cloud.tencent.com/document/product/378/3629)，如果为个人认证请登录控制台申请短信正文模版。
        >- 修改短信签名，仅当正文模版为待审核或已拒绝状态时，才能进行修改，已审核通过的正文模版不支持修改。

        :param request: Request instance for ModifySmsTemplate.
        :type request: :class:`tencentcloud.sms.v20190711.models.ModifySmsTemplateRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.ModifySmsTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySmsTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySmsTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PullSmsReplyStatus(self, request):
        """拉取短信回复状态。

        :param request: Request instance for PullSmsReplyStatus.
        :type request: :class:`tencentcloud.sms.v20190711.models.PullSmsReplyStatusRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.PullSmsReplyStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PullSmsReplyStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PullSmsReplyStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PullSmsReplyStatusByPhoneNumber(self, request):
        """拉取单个号码短信回复状态。

        :param request: Request instance for PullSmsReplyStatusByPhoneNumber.
        :type request: :class:`tencentcloud.sms.v20190711.models.PullSmsReplyStatusByPhoneNumberRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.PullSmsReplyStatusByPhoneNumberResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PullSmsReplyStatusByPhoneNumber", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PullSmsReplyStatusByPhoneNumberResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PullSmsSendStatus(self, request):
        """拉取短信下发状态。

        :param request: Request instance for PullSmsSendStatus.
        :type request: :class:`tencentcloud.sms.v20190711.models.PullSmsSendStatusRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.PullSmsSendStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PullSmsSendStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PullSmsSendStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PullSmsSendStatusByPhoneNumber(self, request):
        """拉取单个号码短信下发状态。

        :param request: Request instance for PullSmsSendStatusByPhoneNumber.
        :type request: :class:`tencentcloud.sms.v20190711.models.PullSmsSendStatusByPhoneNumberRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.PullSmsSendStatusByPhoneNumberResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PullSmsSendStatusByPhoneNumber", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PullSmsSendStatusByPhoneNumberResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SendSms(self, request):
        """短信发送接口，用户给用户发短信验证码、通知类短信或营销短信。


        :param request: Request instance for SendSms.
        :type request: :class:`tencentcloud.sms.v20190711.models.SendSmsRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.SendSmsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SendSms", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SendSmsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SendStatusStatistics(self, request):
        """统计用户发送短信的数据。

        :param request: Request instance for SendStatusStatistics.
        :type request: :class:`tencentcloud.sms.v20190711.models.SendStatusStatisticsRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.SendStatusStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SendStatusStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SendStatusStatisticsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SmsPackagesStatistics(self, request):
        """用户套餐包信息统计。

        :param request: Request instance for SmsPackagesStatistics.
        :type request: :class:`tencentcloud.sms.v20190711.models.SmsPackagesStatisticsRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.SmsPackagesStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SmsPackagesStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SmsPackagesStatisticsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)