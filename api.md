
###1.提交成绩接口
url: /api/submit_quiz

请求参数：
user_id ：用户id（传9527即可）
quiz_id ：测试id
error_words ：错误单词列表
score ：得分

返回数据：
    {"r":"success"}

###2.获取最新测试单词列表
url：/api/get_last_quiz

请求参数：
暂无

返回数据：
