# -*- coding: utf-8 -*-
"""Configuration for Wiki
"""

# For Maverick
site_prefix = "https://wiki.imalan.cn/"
source_dir = "../src/"
build_dir = "../dist/"
template = {
    "name": "Kepler",
    "type": "local",
    "path": "../Kepler"
}
index_page_size = 10
archives_page_size = 20
enable_jsdelivr = {
    "enabled": True,
    "repo": "AlanDecode/site-Wiki@gh-pages"
}
category_by_folder = True
for_manual_build_trigger = 1

# 站点设置
site_name = "無知識 | 三無計劃"
site_logo = "${static_prefix}android-chrome-512x512.png"
site_build_date = "2017-06-29T12:00+08:00"
author = "熊猫小A"
email = "hi@imalan.cn"
author_homepage = "https://www.imalan.cn"
description = "熊猫小A的Wiki站点"
key_words = ['Maverick', '熊猫小A', 'Galileo', 'wiki']
language = 'zh-CN'

valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "2to78D9NRkvN8CTRtIneOcXL-gzGzoHsz",
    "appKey": "ws5n5WDCDFVg5rhvqPceRiuA",
    "visitor": True,
    "recordIP": True,
    "placeholder": "请不吝赐教"
}

external_links = [
    {
        "name": "TRIPLE NULL",
        "url": "https://www.imalan.cn",
        "brief": "三是虚指。至于是哪三无，我唔知。"
    },
    {
        "name": "BLOG",
        "url": "https://blog.imalan.cn",
        "brief": "熊猫小A的博客。隶属于「三无计划」。"
    },
    {
        "name": "LAB",
        "url": "https://lab.imalan.cn",
        "brief": "熊猫小A的实验室。隶属于「三无计划」。"
    },
    {
        "name": "GITHUB",
        "url": "https://github.com/AlanDecode",
        "brief": "My GitHub"
    },
    {
        "name": "CHANNEL",
        "url": "https://t.me/triple_null",
        "brief": "熊猫小A的广播。隶属于「三无计划」。"
    }
]
nav = [
    {
        "name": "HOME",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "ARCHIVES",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "ABOUT",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/AlanDecode",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/AlanDecode",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/5245109677/",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
<link rel="dns-prefetch" href="//static.imalan.cn" />
<link rel="stylesheet" href="${static_prefix}brand_font/embed.css" />
<style>.brand{font-family:FZCuJinLFW,serif;font-weight: normal!important;}</style>
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black">
<link rel="apple-touch-icon" sizes="180x180" href="${static_prefix}apple-touch-icon.png?v=PY43YeeEKx">
<link rel="icon" type="image/png" sizes="32x32" href="${static_prefix}favicon-32x32.png?v=yyLyaqbyRG">
<link rel="icon" type="image/png" sizes="16x16" href="${static_prefix}favicon-16x16.png?v=yyLyaqbyRG">
<link rel="mask-icon" href="${static_prefix}safari-pinned-tab.svg?v=yyLyaqbyRG" color="#505050">
<link rel="shortcut icon" href="${static_prefix}favicon.ico?v=yyLyaqbyRG">
<meta name="application-name" content="無知識">
<meta name="apple-mobile-web-app-title" content="無知識">
<meta name="msapplication-TileColor" content="#000000">
<meta name="theme-color" content="#000000">
<meta name="baidu-site-verification" content="Or6aUYr0De" />
'''

footer_addon = r'''
<a no-style href="http://beian.miit.gov.cn" target="_blank">京ICP备18000133号-1</a> | 
<a no-style href="https://www.upyun.com" target="_blank">又拍云</a>
'''

body_addon = r'''
<script>
(function(){
    var bp = document.createElement('script');
    var curProtocol = window.location.protocol.split(':')[0];
    if (curProtocol === 'https') {
        bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
    }
    else {
        bp.src = 'http://push.zhanzhang.baidu.com/push.js';
    }
    var s = document.getElementsByTagName("script")[0];
    s.parentNode.insertBefore(bp, s);
})();
</script>
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?5735ca789e45ace74acc43d939504ebd";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
</script>
'''