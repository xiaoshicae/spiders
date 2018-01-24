# --*-- encoding:utf-8 --*--
from lxml import etree
import re

content_string = """
<!doctype html>
<html>
	<head>
		<meta charset="utf-8" />
		<title>杭州阿里巴巴广告有限公司_11315_信用档案_信用报告_信用分值_信用评级_怎么样_好不好_信用_信誉_投诉_电话-1</title>
		<meta name="keywords" content="杭州阿里巴巴广告有限公司,11315征信 11315绿盾 信用档案,信用报告,信用评级，信用分值,信用等级,投诉,举报,风险,信用,信誉,好不好,怎么样,资质,质量,黑名单,征信,征信机构，11315征信系统，企业信用查询网" />
		<meta name="description" content="杭州阿里巴巴广告有限公司,11315绿盾,信用编码：12821540,简介：" />

		<script type="text/javascript">
			function nofind(src,dom){var newsrc = src+"_mark";if(!src){newsrc="/images/no_qualifi.jpg";};dom.src=newsrc;dom.onerror=function(){dom.src="/images/no_qualifi.jpg";};}
		</script>
		<script type="text/javascript" src="http://api.map.baidu.com/api?v=2.0&ak=m6oLN8CbTG4b64Kcbr186EZS"></script>

		<link  rel="stylesheet" type="text/css" href="/css/common.css?2017042401" /><link  rel="stylesheet" type="text/css" href="/css/archives/content.css?2017081401" /><link  rel="stylesheet" type="text/css" href="/css/archives/fieldCom.css?20170121" /><link  rel="stylesheet" type="text/css" href="/css/archives/qc.css?20170121" /></head>

	<body>
    	<div id="header">
    <div class="hBox">
        <div class="head_cen">
            <input type="hidden" value="" id="userLogin" name="userLogin">
            <input type="hidden" value="11315.com" id="cookie_domain" name="cookie_domain">
            <p class="fl"><a href="http://www.11315.com/message" target="_blank">项目合作</a></p>
            <p class="fl pl50"><a href="http://app.11315.com" target="_blank">企业信用APP</a></p>
            <ul class="ri">
            	<li><a class="link_a" href="/company/register" target="_blank">我要加入</a></li>
                 <li><a href="http://www.11315.com/comment/index" target="_blank">我要维权</a><span>|</span></li>
                 <li id="li_kinds"><a href="/company/register" target="_blank">注册</a> <a href="http://admin.11315.com" target="_blank">登录</a><a href="/company/findpass" target="_blank">找回密码</a><span>|</span></li>
                 <li><a href="javascript:void(0);" id="homepage">设为首页</a> <a href="javascript:void(0);"  id="favorite">加为收藏</a></li>
            </ul>
        </div>
    </div>
    <div class="logo search">
        <h1 class="fl"><a href="http://www.11315.com"><img src="/images/logo-1.png?2016052301"></a></h1>
        <div class="searchbox">
        <form target="_blank" method="get" action="http://www.11315.com/newsearch" style="zoom: 1;">
                 <input type="hidden" value="选择地区" name="regionMc" id="regionMc">
                 <input type="hidden" value="1" id="searchType" name="searchType">
                 <input type="hidden" value="" id="regionDm" name="regionDm">
                 <input type="hidden" value="1" id="searchTypeHead" name="searchTypeHead">
                 <ul class="search_tab" id="search_tab">
	                <li class="tab_on" type="1"><a href="javaScript:void(0)">企业名称</a></li>
	                <li class="" type="2"><a href="javaScript:void(0)">信用编码</a></li>
	                <li class=""  type="3"><a href="javaScript:void(0)">法定代表人</a></li>
	                <li class=""  type="4"><a href="javaScript:void(0)">股东</a></li>
	                <li class=""  type="5"><a href="javaScript:void(0)">失信被执行人</a></li>
                 </ul>
                <div style=" border: 2px solid #0C6532;border-radius: 0 0 0 3px;zoom: 1; float: left;">
                    <div class="inputbox">
                        <input type="text" id="search-input" value="请输入企业名称" class="init" name="name"  autocomplete="off">
                    </div>
                    <div id="allAreaD" class="inputarea allAreaS"> <span class="f-csp" id="showarea">选择地区</span>
                        <div class="area-wrap">
                            <div class="tabs-wrap">
                                <ul class="tabs-list">
                                    <li><a id="allProvince" href="#province">省份</a></li>
                                    <li><a id="allCity" href="#city">城市</a></li>
                                    <li><a id="allCounty" href="#country">区县</a></li>
                                </ul>
                                <a href="http://s.11315.com" class="highsearch">高级</a> <a href="javascript:void(0);" id="blackCity">清除</a>
                            </div>
                            <div class="cons-wrap">
                                <div id="province">
                                    <ul class="cons-list">
                                </div>
                                <div id="city">
                                    <ul class="cons-list">
                                    </ul>
                                </div>
                                <div id="country">
                                    <ul class="cons-list">
                                    </ul>
                                </div>
                            </div>
                            </div>
                    </div>
                </div>
                <div class="inputbtn">
                    <input type="button" id="head-submit" class="searchbtn" value="搜&nbsp;索">
                </div>
            </form>
            <div id="slogan"> 查企业信用，到11315.com </div>
        </div>
    </div>
    <div id="nav">
    	<ul class="ulNav" id="ulNav">
    		<li >
        	  <a href="http://www.11315.com">首页</a>
        	</li>
        	<li ><a href="http://www.11315.com/infnews/24" target="_blank">征信新闻</a></li>
            <li ><a href="http://www.11315.com/al/m" target="_blank">媒体热评</a></li>
            <li ><a href="http://www.11315.com/rankalllist" target="_blank">行业展示</a></li>
            <li ><a href="http://city.11315.com" target="_blank">城市信用</a></li>
             <li ><a href="http://www.11315.com/lawyer" target="_blank">律师联盟</a></li>
            <li class="li-img" ><a href="http://www.11315.com/comment/index">
            <img src="/images/ts.gif">
			</a></li>
            <li ><a href="http://www.11315.com/infnews/51" target="_blank">政策法规</a></li>
			<li id="liaboutus" ><a href="http://www.11315.com/about/n/about_index" target="_blank">业务介绍</a></li>
        </ul>
       </div>
</div>
<script src="/js/lib/jQueryv1.10.2.js"></script>
<!-- Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36 -->
<div class="tit_main">
<!--对比企业弹出框 -开始-->
	<div class="record_contrast" style="display: none;">
		<div class="contrast_title"><a style="cursor: pointer;"><img class="closeContrast" src="/images/archives/contrast_close01.jpg"></a>[<span class="contrastNum">0</span>&frasl;4]对比框</div>
	    <ul>
	        <li class="li_special contrast_jia">
	        	<a class="addContrastCompany" style="cursor: pointer;"><span class="contrast"><b>&nbsp;</b>信用对比</span></a>
	            <div class="search_con_box" style="display: none;">
	                <input type="text" placeholder="请输入要对比的公司名称" class="required" title="公司名称" id="companyName" name="companyName">
	                <div id="searchcompaydiv"></div>
	            </div>
	        </li>
	        <li class="li_special"><a class="btn_icon" href="javascript:void(0);">开始对比</a><a class="link_color" style="cursor: pointer;">清空对比栏</a></li>
	    </ul>
	</div>
	<!--对比企业弹出框 -开始-->
	<div class="record_tit">
		<div class=" record_tit_l fl">
			<div class="photo">
				<img src="/images/archives/tit_logo_03.jpg" width="160" height="125"/>
				</div>
			<div class="rec_tit fl">
				<input type="hidden" id="gshUuidIndex" name="gshUuidIndex" value="c3aae870-753f-44c1-9978-a1b905987e5c">
						<h1>
						<!-- <a href="http://12821540.11315.com" target="_blank" title="广西油漆集团公司"> 公司</a> -->
						<a class="rec_h1" href="http://12821540.11315.com" target="_blank" title="杭州阿里巴巴广告有限公司">
							杭州阿里巴巴广告有限公司</a>
						<a href="/toManageUserMessage/12821540" target="_blank" class="rec_guestbook"><span></span>访客留言</a>
						<a class="rec_data" href="http://www.11315.com/company/register?bh=12821540" target="_blank">申请认证</a>
							</h1>
				<p class="rec_pad">
					<span>信用网址： <a href="http://12821540.11315.com" target="_blank"><b>12821540.11315.com</b></a></span>
					</p>
				<p class="rec_p">
					<span>私营有限责任公司(自然人控股或私营性质企业控股)</span>
					<span class="rec_blue">成立历史第<span class="span_borld">12&nbsp;</span>年</span>
					</p>
			</div>
		</div>
		<div class=" record_tit_r ri">
			<ul>
				<li class="rec_r_buta">
					<a href="/toCompanyComment/12821540" target="_blank"><span></span>我要评价</a></li>
				<li class="rec_r_but">
					<a class="addToContrast" style="cursor: pointer;" v="%s"><span></span>信用对比</a></li>
			</ul>
			<p>
				<a href="/companyHierarchy/12821540/1" target="_blank" class="m_branch" title="代理分销体系"></a>
				<a href="http://admin.11315.com" target="_blank" class="m_logo" title="立信标识"></a>
				<a id="moreTaba" style="cursor: pointer;"><span class="m_more"></span>更多</a>
			</p>
		</div>
		<div class="pop" style="display: none;">
	   		<h2><span class="clostBtn"></span>档案功能导航</h2>
			    <ul>
			    	<li><a href="/toCompanyComment/12821540" target="_blank"><span class="p_eva"></span>我要评价</a></li>
			        <li><a href=""><span class="p_ratio"></span>信用对比</a></li>
			        <li><a href="/downLoadReport/%s" target="_blank"><span class="p_talk"></span>信用报告</a></li>
			        <li><a href="/companyHierarchy/12821540/1" target="_blank"><span class="p_proxy"></span>代理分销体系</a></li>
			        <li><a href="http://admin.11315.com" target="_blank"><span class="p_logo"></span>立信标识</a></li>
			    </ul>
	   		<h2 class="taRight"><b>查企业信用，到11315.com</b></h2>
		</div>
		<div class="cl"></div>
	</div>
</div>
<script src="/js/searchCompany4Contrast.js?20140410"></script>
<script type="text/javascript">
$(".btn_icon").click(function(){
	var contrastLen = $(".tit_main .contrastCompany").length;
	if(contrastLen!=0){
		window.open("/companyContrast");
	} else{
		alert('请添加一个比对企业！');
		return;
	}
});
// 更多功能导航显示和隐藏
$("#moreTaba").click(function(e){
	$(".pop").toggle();
	$(".pop").click(function(e){
		e.stopPropagation();
	});
	e.stopPropagation();
	$("html").click(function(){
		$(".pop").hide();
	});
});
// 更多功能导航关闭
$(".clostBtn").click(function(){
	$(".pop").hide();
});
// 加入对比处理
$(".addToContrast").click(function(){
	$.ajax({
		type : "post",
		dataType : "json",
		url : "/addToContrast",
		data : {
			companyId : $(this).attr("v")
		},
		success : function(result) {
			if(!result.err){
				if(result.message){
					alert(result.message);
				}

				var length = result.value.length;
				if(length == 4){
					$(".contrast_jia").hide();
				}
				$("li.contrastCompany").remove();
				for(var i=0; i<result.value.length; i++){
					var bhLink = "http://" + result.value[i].bh + ".11315.com";
					$(".contrast_jia").before("<li class='contrastCompany'><div class='img_close displaynone'></div><a href='" + bhLink + "' target='_blank' v='" + result.value[i].id + "'>" + result.value[i].realName +  "</a></li>");
				}
				// 企业列表hover处理
				$(".contrastCompany").hover(function(){
					$(this).find(".img_close").removeClass("displaynone");
					$(this).addClass("addhover");
				}, function(){
					$(this).find(".img_close").addClass("displaynone");
					$(this).removeClass("addhover");
				});
				// 移除对比列表中的企业
				$(".img_close").click(function(){
					var $this = $(this);
					var companyId = $this.next("a").attr("v");
					$.ajax({
						type : "post",
						dataType : "json",
						url : "/removeContrastCompany",
						data : {companyId : companyId},
						success : function(result) {
							initContrast();
						}
					});
				});
				$(".contrastNum").text(length);
				$(".record_contrast").show();
			} else {
				alert(result.message);
			}
		},
		error:function(xhr,ajaxOptions,throwError){}
	});
});
// 点击“加入对比”的处理
$(".addContrastCompany").click(function(e){
	$(".search_con_box").show();
	$(".search_con_box").click(function(e){
		e.stopPropagation();
	});
	e.stopPropagation();
	$("html").click(function(){
		$(".search_con_box").hide();
	});
});
$(".closeContrast").click(function(){
	$(".record_contrast").hide();
});
// 清空对比栏
$(".link_color").click(function(){
	$.ajax({
		type : "post",
		dataType : "json",
		url : "/clearContrast",
		success : function(result) {
			$(".contrast_jia").show();
			$(".contrastNum").text(0);
			$("li.contrastCompany").remove();
		}
	});
});

// 对比列表初始化
var initContrast = function(){
	$.ajax({
		type : "post",
		dataType : "json",
		url : "/getContrastList",
		success : function(result) {
			if(result.value){
				var length = result.value.length;
				if(length == 4){
					$(".contrast_jia").hide();
				} else {
					$(".contrast_jia").show();
				}
				$("li.contrastCompany").remove();
				for(var i=0; i<result.value.length; i++){
					var bhLink = "http://" + result.value[i].bh + ".11315.com";
					$(".contrast_jia").before("<li class='contrastCompany'><div class='img_close displaynone'></div><a href='" + bhLink + "' target='_blank' v='" + result.value[i].id + "'>" + result.value[i].realName +  "</a></li>");
				}
				// 企业列表hover处理
				$(".contrastCompany").hover(function(){
					$(this).find(".img_close").removeClass("displaynone");
					$(this).addClass("addhover");
				}, function(){
					$(this).find(".img_close").addClass("displaynone");
					$(this).removeClass("addhover");
				});
				// 移除对比列表中的企业
				$(".img_close").click(function(){
					var $this = $(this);
					var companyId = $this.next("a").attr("v");
					$.ajax({
						type : "post",
						dataType : "json",
						url : "/removeContrastCompany",
						data : {companyId : companyId},
						success : function(result) {
							initContrast();
						}
					});
				});
				$(".contrastNum").text(length);
				$(".record_contrast").show();
			} else {
				$(".contrast_jia").show();
				$(".contrastNum").text(0);
				$("li.contrastCompany").remove();
			}
		}
	});
}
if($(".xscreditdays").length>0){
	var cid= "%s";
	$.getJSON("/creditdays/"+cid,{}, function(json){
		if(!json.err && json.message){
			var message=Number(json.message);
			$(".xscreditdays").text(Math.ceil(message/365));
		}
	});
}
initContrast();
</script>
<div id="main">
		   	<div class="content">
		   		<div class="cont_l fl">
					<div class="cont_ltit clearfix">
						<input type="hidden" name="companyId" id="companyId" value="%s" />
						<div class="dang_an"><span>信用编码: 12821540</span> <b>信用档案</b>
						</div>
						<div class="v1Table">
		                    <table cellpadding="0" cellspacing="0" class="v1Table01">
		                        <col width="12%">
                                <col width="35%">
                                <col width="12%">
                                <col width="12%">
                                <col width="11%">
                                <col width="18%">
		                        <tr>
		                            <th>单位名称</th>
				                   	<!-- <th> </th> -->
				                   	<!-- <th> </th> -->
		                            <th colspan="4" class="th01" title="杭州阿里巴巴广告有限公司">
		                            	杭州阿里巴巴广告有限公司</th>
		                            <th rowspan="3" class="th_img"><a target="_blank" href="/imgaCompanyTdcodeBig?bh=12821540&v=2017072701"><img alt="点击查看大图" src="/imgaCompanyTdcode110?bh=12821540"  height="100" width="100" /></a></th>
		                        </tr>
		                        <tr style="display: none;">
		                            <th>分值</th>
		                            <td>
		                            	19.50</td>
		                            <th>信用等级</th>
		                            <td colspan="2">
		               				<a>(信息量不足未予评级)</a> </td>
		                        </tr>
		                        <tr style="display: none;">
		                            <th>信用等级</th>
		                            <td colspan="5">
		               				<a>(信息量不足未予评级)</a> </td>
		                        </tr>
		                        <tr>
		                            <th>法定代表人</th>
		                            <td>
		                            <p style="background-image: url('http://img.11315.com/companyInfoImg/2015/10/10/qjevo.jpg');display:inline-block;vertical-align:middle;background-position:-144px -4px;width:24px;height:15px;"></p>									</td>
		                            <th class="th02">注册资金</th>
			                            <td style=" border-right: 0">
			                            1000.0万元</td>
										<td style=" border-left: 0">&nbsp;</td>
		                            </tr>
		                        <tr>
		                            <th>行　　业</th>
		                            <td style="overflow: hidden;"  colspan="4">
		                            	广告</td>
		                        </tr>
<tr>
		                            <th>所在区域</th>
		                            <td colspan="2">
		                            	<p style="background-image: url('http://img.11315.com/companyInfoImg/2015/10/10/qjevo.jpg');display:inline-block;vertical-align:middle;background-position:-168px -4px;width:108px;height:15px;"></p>									</td>
		                            <th class="th02">商务网址</th>
		                            <td colspan="2">
		                            	<a style="color:#333" href="" target="_blank"></a>
		                            </td>
		                        </tr>
		                        <tr>
		                        <th>详细地址</th>
		                            <td colspan="5">杭州市滨江区网商路699号1号楼5楼
		                            &nbsp;<a class="maplink" href="javascript:void(0);">查看地图</a></td>
		                        </tr>
		                        <tr>
		                            <th>主营产品</th>
		                            <td colspan="5" style="overflow:hidden;">
		                            	许可经营项目：利用自有www.alibaba.cn和www.alibaba.co</td>
		                        </tr>
		                        <tr>
		                            <th>单位简介</th>
		                            <td colspan="5">
		                            	&nbsp;&nbsp;
                            			<a href="/ac/bs/%s" target="_blank">&gt;&gt;更多商务信息</a>
		                            </td>
		                        </tr>
		                    </table>
		                    </div>
<!-- <h2 class="h2ttl"><span>L1 档案</span></h2> -->
	                	<div class="cont_lcen cont_l_v1">
	                    	<h3 class="h3ttl"><span>含工商/税务/质检/法院/司法/海关/环保/国土/劳动/安检/食药/卫生/科技/版权/教育/住建等全部职能部门</span>1.政府公示信息</h3>
	                    	<div class="v1_title_ul">
 <div style="overflow: hidden;zoom:1; clear: both;">
		                        	<h4 class="v1_title">
			                        	<a href="#">1-1.基本资质</a>
		                        	</h4>
	                        	</div>
<ul class="zizhi-list f-cb zizhi-list-noimg">
	<li><a href="/ac/nofile/%s/1" target="_blank">企业法人营业执照</a></li>
									<li><a href="/ac/nofile/%s/2" target="_blank">组织机构代码</a></li>
									<li><a href="/ac/nofile/%s/3" target="_blank">税务登记证</a></li>
		<li><a href="/ac/nofile/%s/4" target="_blank">银行开户许可证</a></li>
			                        <li><a href="/ac/nofile/%s/5" target="_blank">第三方征信认证</a></li>
			                    </ul>
</div>

	                    	<div class="v1-business">
		                    	<h4>
				                	<a href="#">1-2.工商信息</a></h4>
			                   	<ul>
			                   	<!-- 	<li>基本信息（<a href="" target="_blank">35</a>条）</li>
			                   		<li>股东信息（<a href="" target="_blank">35</a>条）</li>
			                   		<li>出资信息（<a href="" target="_blank">35</a>条）</li>
			                   		<li>主要人员（<a href="" target="_blank">35</a>条）</li>
			                   		<li>分支机构（<a href="" target="_blank">35</a>条）</li>
			                   		<li>动产抵押（<a href="" target="_blank">35</a>条）</li>
			                   		<li>股权出质（<a href="" target="_blank">35</a>条）</li>
			                   		<li>知识产权出质（<a href="" target="_blank">35</a>条）</li>
			                   		<li>股权变更（<a href="" target="_blank">35</a>条）</li>
			                   		<li>其他变更（<a href="" target="_blank">35</a>条）</li>
			                   		<li>抽查检查（<a href="" target="_blank">35</a>条）</li>
			                   		<li>清算信息（<a href="" target="_blank">35</a>条）</li>
			                   		<li>企业年报（<a href="" target="_blank">35</a>条）</li>
			                   		<li>对外投资（<a href="" target="_blank">35</a>条）</li>
			                   		<li>历史法人代表（<a href="" target="_blank">35</a>条）</li>
			                   		<li>历史股东（<a href="" target="_blank">35</a>条）</li>
			                   		<li>司法协查（<a href="" target="_blank">35</a>条）</li>
			                   		<li>工商处罚（<a href="" target="_blank">35</a>条）</li>
			                   		<li>经营异常（<a href="" target="_blank">35</a>条）</li>
			                   		<li>企业状态（<a href="" target="_blank">35</a>条）</li> -->

			                   		<li>基本信息 （<a href="/cil/index/%s" target="_blank">查看</a>）</li>
			                   		<li>股东信息（<a href="/cil/gdl/%s" target="_blank">0</a>条）</li>
			                   		<li>变更信息（<a href="/cil/bgl/%s" target="_blank">0</a>条）</li>
			                   		<li>主要人员（<a href="/cil/kp/%s" target="_blank">0</a>条）</li>
			                   		<li>分支机构（<a href="/cil/org/%s" target="_blank">0</a>条）</li>
			                   		<li>股权出质（<a href="/cil/stockEqu/%s" target="_blank">0</a>条）</li></li>
			                   		<li>动产抵押（<a href="/cil/chatList/%s" target="_blank">0</a>条）</li>
			                   		<li>抽查检查（<a href="/cil/ccjcl/%s" target="_blank">0</a>条）</li>
			                   		<li>清算信息（<a href="/cil/clear/%s" target="_blank">0</a>条）</li>
			                   		<li>工商处罚（<a href="/cil/xzcfgsl/%s" target="_blank">0</a>条）</li>
			                   		<li>其他处罚（<a href="/cil/xzcfqtl/%s" target="_blank">0</a>条）</li>
			                   		<li>经营异常（<a href="/cil/jyycl/%s" target="_blank">0</a>条）</li>
			                   		<li>违法信息（<a href="/cil/yzwfl/%s" target="_blank">0</a>条）</li>
			                   		<li>主管部门（<a href="/cil/zhgbm/%s" target="_blank">0</a>条）</li>
			                   		<li>企业年报（<a href="/cil/annualjiben/%s" target="_blank"></a>条）</li>
			                   	</ul>
	                    	</div>

		                    <h4 class="v1_title">
		                        <p>

									         	共<a href="/acl/qf/%s/1" target="_blank">1</a>条信息
									    </p>
		                    	<a href="/acl/qf/%s" target="_blank">1-3.行政许可资质</a>
							    	</h4>
		                    <h4 class="v1_title">
		                        <p>
		                       	    共<a href="/acl/am/%s/1" target="_blank">9</a>条信息</p>
		                   		<a href="/acl/am/%s" target="_blank">1-4.行政表彰信息</a>
							     	</h4>
		                    <h4 class="v1_title">
		                        <p>
		                        	共<a href="javascript:void(0);" onclick="return false;">&nbsp;</a>条信息</p>
		                   		<a href="javascript:void(0);" onclick="return false;">1-5.行政处罚信息</a>
							   		</h4>


		                    <h4 class="v1_title">
		                        <p>

                                                                                                           共<a href="/acl/v/%s/1" target="_blank">105</a>条信息
										</p>
		                    	<a href="/acl/v/%s" target="_blank">1-6.人民法院的判决信息</a>
									</h4>
		                    <h4 class="v1_title v1_subordinate">
		                        <p>

                                                                                                           共<a href="/acl/v/%s/1" target="_blank">101</a>条信息
										（一审判决<a href="/acl/v/%s/1" target="_blank">99</a>条，二审判决<a href="javascript:void(0);" onclick="return false;">&nbsp;</a>条，再审判决<a href="javascript:void(0);" onclick="return false;">&nbsp;</a>条）</p>
		                    	<a href="/acl/v/%s" target="_blank">判决信息</a>
									</h4>
		                    <h4 class="v1_title v1_subordinate">
		                        <p>

								共<a href="/acl/vf/%s/0" target="_blank">4</a>条信息
										（已结案<a href="javascript:void(0);" onclick="return false;">&nbsp;</a>条，执行中<a href="javascript:void(0);" onclick="return false;">&nbsp;</a>条，其他<a href="/acl/vf/%s/3" target="_blank">4</a>条）</p>
		                    	<a href="/acl/vf/%s" target="_blank">被执行人信息</a>
									</h4>
		                    <h4 class="v1_title v1_subordinate">
		                        <p>

								共<a href="javascript:void(0);" onclick="return false;">&nbsp;</a>条信息
										</p>
			                    <a href="javascript:void(0);" onclick="return false;">失信被执行人信息</a>
									</h4>
		                    <h4 class="v1_title">
		                    <p>
		                        <span>合格率-%</span>
		                        	共<a href="javascript:void(0);" onclick="return false;">&nbsp;</a>条信息（合格<a href="javascript:void(0);" onclick="return false;">&nbsp;</a>条，不合格信息<a href="javascript:void(0);" onclick="return false;">&nbsp;</a>）</p>
		                    	 <a href="javascript:void(0);" onclick="return false;">1-7.质量检查信息</a>
		                        	</h4>
		                    <h3 class="h3ttl">2.行业评价信息</h3>
		                    <h4 class="v1_title">
		                        <p>
		                        	<span>良好率-%</span>
		                        	共<a href="javascript:void(0);" onclick="return false;">&nbsp;</a>条信息（良好<a href="javascript:void(0);" onclick="return false;">&nbsp;</a>条，风险信息<a href="javascript:void(0);" onclick="return false;">&nbsp;</a>条）</p>
		                    	<a href="javascript:void(0);" onclick="return false;">2-1.行业协会(社会组织)评价信息</a>
									</h4>
		           			<h4 class="v1_title">
		                        <p>
		                        	<span>

		                        	良好率-%
		                        	</span>
		                        	共<a href="javascript:void(0);" onclick="return false;">&nbsp;</a>条信息（良好<a href="javascript:void(0);" onclick="return false;">&nbsp;</a>条，负面<a href="javascript:void(0);" onclick="return false;">&nbsp;</a>条）</p>
		                    	<a href="javascript:void(0);" onclick="return false;">2-2.招标投标行业信息</a>
									</h4>
		                   	<h4 class="v1_title v1_subordinate"><p>共<a href="/acl/bid/%s/1" target="_blank"></a>条信息</p>中标信息</h4>
			                <h4 class="v1_title v1_subordinate"><p>共<a href="/acl/bid/%s/2" target="_blank"></a>条信息</p>处罚信息</h4>

		                    <h3 class="h3ttl">3.知识产权信息</h3>
		                    <h4 class="v1_title">
		                        <p>

								共<a href="/acl/p/%s" target="_blank">25</a>条信息
										</p>
		                    	<a href="/acl/p/%s" target="_blank">3-1.商标/专利/著作权信息</a>
									</h4>
		                    <h4 class="v1_title v1_subordinate">
		                        <p>

								共<a href="/acl/p/%s/3" target="_blank">25</a>条信息
										</p>
		                    	<a href="/acl/p/%s/3" target="_blank">商标信息</a>
									</h4>
		                    <h4 class="v1_title v1_subordinate">
		                        <p>

								共<a href="javascript:void(0);" onclick="return false;">&nbsp;</a>条信息
										（发明专利<a href="javascript:void(0);" onclick="return false;">&nbsp;</a>条，实用型新专利<a href="javascript:void(0);" onclick="return false;">&nbsp;</a>条，外观设计专利<a href="javascript:void(0);" onclick="return false;">&nbsp;</a>条）</p>
		                    	<a href="javascript:void(0);" onclick="return false;">专利信息</a>
									</h4>
		                    <h4 class="v1_title v1_subordinate">
		                        <p>

								共<a href="javascript:void(0);" onclick="return false;">&nbsp;</a>条信息
										（软件著作权<a href="javascript:void(0);" onclick="return false;">&nbsp;</a>条，作品著作权<a href="javascript:void(0);" onclick="return false;">&nbsp;</a>条）</p>
		                    	<a href="javascript:void(0);" onclick="return false;">著作权信息</a>
									</h4>
		        			<h4 class="v1_title">
		                        <p>共<a href="javascript:void(0);" onclick="return false;">&nbsp;</a>条信息</p>
								<a href="javascript:void(0);" onclick="return false;">3-2.网站备案信息</a>
		                    </h4>
		                    <h4 class="v1_title">
		                        <p>
		                        	共<a href="javascript:void(0);" onclick="return false;">&nbsp;</a>条信息</p>
		                        <a href="javascript:void(0)" onclick="return false;">3-3.体系/产品/行业认证信息</a>
									</h4>

		                    <h3 class="h3ttl">4.媒体评价信息</h3>
		                    <h4 class="v1_title">
		                        <p>
		                        	<span>良好率-%</span>
		                        	共<a href="javascript:void(0);" onclick="return false;">&nbsp;</a>条信息（良好<a href="javascript:void(0);" onclick="return false;">&nbsp;</a>条，风险信息<a href="javascript:void(0);" onclick="return false;">&nbsp;</a>条）</p>
		                    	<a href="javascritp:void(0);" onclick="return false;">4-1.媒体评价信息</a>
									</h4>
		                     <h4 class="v1_title">
		                        <p>
		                    	   共<a href="javascript:void(0);" onclick="return false;">&nbsp;</a>条信息
		                        </p>

								<a href="javascript:void(0);" onclick="return false;">4-2.媒体信息（关联参考）</a>
		                    </h4>
		                    <h3 class="h3ttl">5.金融信贷信息</h3>
		                    <h4 class="v1_title" id="tradeLendingh4"></h4>
		                    <h4 class="v1_title">
		                        <p>
		                        	<span>良好率-%</span>
		                        	共<a href="javascript:void(0)">&nbsp;</a>条信息（良好<a href="javascript:void(0)">&nbsp;</a>条，逾期信息<a href="javascript:void(0)">&nbsp;</a>条）</p>
		                    	<a href="javascript:void(0);" onclick="return false;">5-2.民间借贷评价信息</a>
									</h4>
		                    <h3 class="h3ttl">6.企业运营信息(银企通功能)</h3>
		                    <h4 class="v1_title">
		                        <p>(该信息涉商业机密，需要获得授权才能查看。)<a class="v1_link" style="float: none" href="/acl/cw/%s" target="_blank">继续查看>></a></p>
		                        <a href="javascript:void(0);" onclick="return false;">6-1.企业财务信息</a></h4>
		                    <h4 class="v1_title">
		                        <p>(专项服务)</p>
		                        <a href="javascript:void(0);" onclick="return false;">6-2.企业管理体系评估信息</a>
		                    </h4>
							<h4 class="v1_title" id="utilitiesh4"></h4>
							<h4 class="v1_title" id="ratepayingh4"></h4>
							<h4 class="v1_title"  id="harmoniousLabor"></h4>
							<h3 class="h3ttl commentDetail">7.市场反馈信息</h3>
		                    <h4 class="v1_title commentDetail" id="commentDetailFirst">
		                        <p>
		                        	<span>好评率0.0%</span>
		                         	共<a href="/acl/c1/%s" target="_blank">1</a>条信息（好评<a href="javascript:void(0)">&nbsp;</a>条，投诉<a href="/acl/c1/%s/3" target="_blank">1</a>条）</p>
		                    	<a style="width: 135px; display: inline-block;" href="/acl/c1/%s" target="_blank">7-1.消费者评价信息</a><a class="v1_link" href="/toCompanyComment/12821540" target="_blank">[我要评论]</a>
									</h4>
		                    <h4 class="v1_title commentDetail">
		                        <p>
		                        	<span>好评率-%</span>
		                        	共<a href="javascript:void(0);" onclick="return false;">&nbsp;</a>条信息（好评<a href="javascript:void(0)">&nbsp;</a>条，投诉<a href="javascript:void(0)">&nbsp;</a>条）</p>
		                    	<a style="width: 135px; display: inline-block;" href="javascript:void(0);" onclick="return false;">7-2.企业之间履约评价</a><a class="v1_link" href="/toCompanyComment/12821540" target="_blank">[我要评论]</a>
									</h4>
		                    <h4 class="v1_title commentDetail">
		                        <p>
		                        	<span>好评率-%</span>
		                        	 共<a href="javascript:void(0)">&nbsp;</a>条信息（好评<a href="javascript:void(0)">&nbsp;</a>条，投诉<a href="javascript:void(0)">&nbsp;</a>条）</p>
		                        <a style="width: 135px; display: inline-block;" href="javascript:void(0);" onclick="return false;">7-3.员工评价信息</a><a class="v1_link" href="/toCompanyComment/12821540" target="_blank">[我要评论]</a>
									</h4>
		                    <h4 class="v1_title commentDetail">
		                        <p>
		                        	<span>好评率-%</span>
		                        	共<a href="javascript:void(0);" onclick="return false;">&nbsp;</a>条信息（好评<a href="javascript:void(0)">&nbsp;</a>条，投诉<a href="javascript:void(0)">&nbsp;</a>条）</p>
	<a style="width: 135px; display: inline-block;" href="javascript:void(0);" onclick="return false;">7-4.其他</a><a class="v1_link" href="/toCompanyComment/12821540" target="_blank">[我要评论]</a>
		</h4>
		                    <div id="echartscontainerPre"></div>
		                    <div id="echartscontainer" style="min-width: 250px; height: 250px;display: none;margin-top: 5px;" chartload="false"></div>
	</div>
	<script type="text/javascript">
		$(".toOpenInfo").click(function(){
			$(".toOpenInfo").hide();
			$(".toCloseInfo").show();
			$(".v_none").show();
		});

		$(".toCloseInfo").click(function(){
			$(".toOpenInfo").show();
			$(".toCloseInfo").hide();
			$(".v_none").hide();
		})
	</script>
<!-- <h2 class="h2ttl"><span>L2 档案</span></h2> -->
		               <div class="cont_lcen cont_l_v1 cont_lcen_top">
		                   <!-- 勿删，v2数目显示临时改成异步查询，待数据导入完毕，更新分值表完毕，再改成直接查询 -->
		                    <input type ="hidden" id="v2CompanyId" name="v2CompanyId" value="%s">
		                    <div class="v1_com_text">
		                        <p>综合评价：<br>
		                            <span>依据国务院社会信用体系建设要求及《征信业管理条例》规定，对信用档案中依法采集的信用信息按照统一模型标准计算。
		                            质量检查0条风险信息记录、 合格率 - %，
		                            行政处罚 0 条风险信息记录、 良好率 100.0 %，
		                            媒体评价信息 0 条风险信息记录、 良好率 - %，
		                            市场实名反馈有 1 条投诉信息、 好评率 0.0 %。</span></p>
		                        <p>提醒该信用报告的使用者：<br>
		                            <span>一、请密切关注交易对方的各项信用指标，整体把握信用风险，以保障交易安全；</span>
		                           <span>二、请随时关注交易对方的信用动态变化，及时把握信用趋势，以掌控商业风险。</span></p>
		                        <p>
		                        绿盾声明：<br/>
		                       <span> 本机构为中国人民银行备案的第三方征信机构，不对任何企业做任何主观评价，只是信用信息的采集者、计算者，恪守“让数据说话，用事实作证”的征信理念，通过采集各方评价信用信息，并以统一的数学模型计算得出客观信用分值和评级，供使用者参考。
</span>
		                        </p>
		                        <p style=" color: #333;"><span>信用是企业的生命线；信用档案是企业整体信用状况的动态记录，是企业获得商业信任、促成交易的基础，是大众消费、交易决策的重要参考依据和公平保障体系。</span></p>
		                        <div style="overflow: hidden">
		                            <div class="div_bottom">
		                                绿盾征信(北京)有限公司<br>
		                                报告时间： 2017年09月26日15时16分14秒<a href="/downLoadReport/%s" target="_blank">下载信用报告</a> </div>
		                        </div>
		                    </div>
		                </div></div>


	<!--分享样式-开始-->
		<style type="text/css">
		.fenx { overflow:hidden; clear: both;}
		.bdsharebuttonbox {float: right;}
		</style>
	<!--分享样式-结束-->

<div class="fenx">
	<div class="bdsharebuttonbox fenx_line" data-tag="share_1">
		<span style="float: left;padding-top: 5px;">分享到:</span>
		<a class="bds_weixin" data-cmd="weixin"></a>
		<a class="bds_mshare" data-cmd="mshare"></a>
		<a class="bds_qzone" data-cmd="qzone" href="#"></a>
		<a class="bds_tsina" data-cmd="tsina"></a>
		<a class="bds_baidu" data-cmd="baidu"></a>
		<a class="bds_renren" data-cmd="renren"></a>
		<a class="bds_tqq" data-cmd="tqq"></a>
		<a class="bds_more" data-cmd="more">更多</a>
		<a class="bds_count" data-cmd="count"></a>
	</div>
</div>


	<script>window._bd_share_config={"common":{"bdSnsKey":{},"bdText":"","bdMini":"2","bdMiniList":["weixin","mshare","qzone","sqq","tsina","bdysc","renren","tqq","bdxc","kaixin001","tqf","tieba","douban","tsohu","taobao","qingbiji","isohu","wealink","ty","copy","print"],"bdPic":"","bdStyle":"0","bdSize":"16"},"share":{}};with(document)0[(getElementsByTagName('head')[0]||body).appendChild(createElement('script')).src='http://bdimg.share.baidu.com/static/api/js/share.js?v=89860593.js?cdnversion='+~(-new Date()/36e5)];</script>
</div>
				<div class="cont_r ri">
				    <div class="search_con_right">
        	<div id="topCompanyList" style="display: none">
               </div>
           <div class="ss_box">
            	<p class="p_title"><a target="_blank" href="/infnews/63" class="more">更多&gt;&gt;</a>视频联播</p>
                <ul>
                	<li><a href="/infnews/show-45217" title="李克强主持召开国务院常务会议部署加快建设社会信用体系"  target="_blank">李克强主持召开国务院常务会议部署...</a></li>
            	    <li><a href="/infnews/show-77203" title="查询企业信用 到11315.com"  target="_blank">查询企业信用 到11315.com</a></li>
            	    <li><a href="/infnews/show-93749" title="绿盾征信档案正逐步成为企业标配"  target="_blank">绿盾征信档案正逐步成为企业标配</a></li>
            	    <li><a href="/infnews/show-93743" title="安徽省无为县推广应用绿盾征信企业信用档案"  target="_blank">安徽省无为县推广应用绿盾征信企业...</a></li>
            	    <li><a href="/infnews/show-93523" title="征信头条第3期：绿盾企业信用档案正成为食品界守信企业的“标配”"  target="_blank">征信头条第3期：绿盾企业信用档案...</a></li>
            	    <li><a href="/infnews/show-93344" title="绿盾征信报告：招投标的必备王牌"  target="_blank">绿盾征信报告：招投标的必备王牌</a></li>
            	    <li><a href="/infnews/show-93343" title="绿盾征信受邀为临汾中小企业讲解信用体系建设"  target="_blank">绿盾征信受邀为临汾中小企业讲解信...</a></li>
            	    <li><a href="/infnews/show-93284" title="2017昆明社会组织竞信论坛成功举办"  target="_blank">2017昆明社会组织竞信论坛成功举办</a></li>
            	    <li><a href="/infnews/show-93283" title="绿盾征信助力青州“信用城市”建设"  target="_blank">绿盾征信助力青州“信用城市”建设</a></li>
            	    <li><a href="/infnews/show-92684" title="绿盾征信贵州分公司荣获企业50强称号"  target="_blank">绿盾征信贵州分公司荣获企业50强称...</a></li>
            	    </ul>
            </div>
            <div class="ss_box lastSideDiv">
            	<p class="p_title"><a target="_blank" href="/infnews/52" class="more">更多&gt;&gt;</a>绿盾征信系统规则</p>
                <ul>
                	 <li><a href="/infnews/show-2437" title="全国征信系统（11315.com）大数据、第三方社会征信平台"  target="_blank">全国征信系统（11315.com）大数据...</a></li>
		        	<li><a href="/infnews/show-434" title="运营模式及收费标准"  target="_blank">运营模式及收费标准</a></li>
		        	<li><a href="/infnews/show-5046" title="查询企业信用档案的三种方式"  target="_blank">查询企业信用档案的三种方式</a></li>
		        	<li><a href="/infnews/show-449" title="企业征信系统问题解答"  target="_blank">企业征信系统问题解答</a></li>
		        	<li><a href="/infnews/show-412" title="企业信用档案内容的组成结构"  target="_blank">企业信用档案内容的组成结构</a></li>
		        	<li><a href="/infnews/show-447" title="在线发布信息的实名制管理办法"  target="_blank">在线发布信息的实名制管理办法</a></li>
		        	<li><a href="/infnews/show-445" title="企业信用档案的功能"  target="_blank">企业信用档案的功能</a></li>
		        	<li><a href="/infnews/show-444" title="信用信息异议制度"  target="_blank">信用信息异议制度</a></li>
		        	<li><a href="/infnews/show-430" title="率先建立起的大数据企业征信模式"  target="_blank">率先建立起的大数据企业征信模式</a></li>
		        	<li><a href="/infnews/show-411" title="社会各阶层对信用档案的支持和迫切需求"  target="_blank">社会各阶层对信用档案的支持和迫切...</a></li>
		        	</ul>
            </div>
		</div>  </div>
				</div>
		</div>
		<div id="mapcontainer">
			<div id="container"></div>
			<div id="closemapcontainer" class="close" style="top:9px;*top:10px;right:-809px;float: right;cursor: pointer; position:absolute;">
				<img src="/images/close1.jpg">
			</div>
		 <div class="pop_up_bg"style="z-index:-10000000; _width:30%;"></div>
		</div>
		<div id="footer">
    <input type="hidden" id="ajaxQueryTopCompanyId" name="ajaxQueryTopCompanyId" value="%s">
    <input type="hidden" id="isAjaxQueryTopCompany" name="isAjaxQueryTopCompany" value="true">
    <div class="footer_top">
        <p>根据《征信业管理条例》第21条，绿盾全国企业征信系统将政府相关部门依据《政府信息公开条例》公开的行政监管信息进行采集、整理、保存、加工，并吸纳市场主体、交易对方、行业协会（社团组织）、法院、主流媒体及实名制下广大消费者发布的评价信息，为境内曾在登记机关注册过的8000多万家信息主体（包括开业、在营、歇业、吊销、注销的企业、个体工商户、农民专业合作社、民办非企业、社团组织、事业单位等）建立信用档案，对信息主体的信用状况进行客观、动态记录，免费供大众查询。</p>
    </div>
    <div id="footer_bot">
    <ul class="">
        <li class="f_li01">
        	运营管理：绿盾征信(北京)有限公司<br>
        	大数据支持：绿盾信息股份有限公司<br>
        	中华人民共和国《企业征信业务经营备案证》编号：10031
        </li>
        <li class="">
        	<a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010202001315"><img style="margin-top: -3px;" src="/images/ghs.png"> 京公网安备：11010202001315</a></br>
        	工信部备案编号：京ICP备12027153号<br>
        	<a style="color:#b70000;" href="http://www.11315.com/objection" target="_blank">【异议反馈】</a>
        	<a style="color:#b70000;" href="/search/searchLeague" target="_blank">【信用搜索联盟】</a><br/>
        	<a style="color:#b70000;" href="http://www.11315.com/message/presidentBox" target="_blank">【总裁信箱】</a>
        	<a style="color:#b70000;" href="/message/report" target="_blank">【举报工作人员】</a>
        </li>
        <li>
        	服务电话 400-07-11315<br>
        	征信受理 <a href="#">315@11315.com</a><br>
        	合作申请 <a href="#"> 123@11315.com</a><br>
        	<a style="color:#b70000;" href="/message" target="_blank">【项目合作申请】</a>
        </li>
    </ul>
    </div>
    <div id="footer_bota">
    <ul>
    	<li class="f_img">
        	<a href="tencent://message/?uin=412300749&Site=&Menu=yes" target="_blank" class="qq">
        		QQ客服1
        	</a>
        	<a href="tencent://message/?uin=249422253&Site=&Menu=yes" target="_blank" class="qq">
        		QQ客服2
        	</a>
        </li>
        <li>
        	<span><a href="http://app.11315.com" target="_blank"><img src="/images/qdcode/test_Android.jpg" width="78" height="78"><br/>安卓版手机APP下载</a></span>
        	<span><a href="http://app.11315.com" target="_blank"><img src="/images/qdcode/test_iOS.jpg" width="78" height="78"><br/>苹果版手机APP下载</a></span>
        </li>
        <li class="f_img f_img01">
	         		<a href="http://www.11315.com/webSiteCredit/21662065?t=3c6132224e55257041cfe56edda2126a75180bcdd7ce9216b4a150b58972b079" target="_blank">
					<img src="http://static.11315.com/credit/web_site_mb_size1.gif" style="border: medium none;" alt="11315可信网站认证">
					</a>
	         		<a href="https://ss.knet.cn/verifyseal.dll?sn=e15040311010258215twkd000000&ct=df&a=1&pa=0.21488783322274685" target="_blank">
		        		<img src="/images/common/footer_kxicon.png" width="83" height="30">
		        	</a>
		        	<a id='___szfw_logo___' href='https://credit.szfw.org/CX20150821011013120561.html' target='_blank'>
		        		<img src="/images/common/footer_cx.png" border='0' />
		        	</a>
			        <script type='text/javascript'>(function(){document.getElementById('___szfw_logo___').oncontextmenu = function(){return false;}})();</script>
			         </li>
    </ul>
    </div>
</div>
<div id="loginDiv" style="display:none;">
	<div class="pop_up_box deng_lu" >
	    <div class="pop_up">
	        <h2>登录</h2>
	        <div class="pop_width">
	            <form>
	                <ul class="radio_ul" style=" margin-top: 40px;">
	                    <li>
	                        <label for="fConsumer">
	                            <input type="radio" checked = true value="0" name="userType" class="fConsumer"/>
	                            	消费者用户
	                        </label>
	                    </li>
	                    <li>
	                        <label for="fAdmin">
	                            <input type="radio" value="1" name="userType" class="fAdmin"/>
	                            	企业用户
	                        </label>
	                    </li>
	                </ul>
	                <ul class="pop_login">
	                    <li>账号：
	                        <input type="text" style="color:#c1bfbf" value="手机号/用户名/邮箱" id="loginName" name="loginName" class="fName" onFocus="if(this.value=='手机号/用户名/邮箱'){this.value=''};this.style.color='#333';" onBlur="if(this.value==''||this.value=='手机号/用户名/邮箱'){this.value='手机号/用户名/邮箱';this.style.color='#c1bfbf';}" />
	                    </li>
	                    <li>密码：
	                        <input type="password" style="color:#c1bfbf" value="" id="passWord" name="passWord" class="fPass"  onFocus="if(this.value==''){this.value=''};this.style.color='#333';" onBlur="if(this.value==''||this.value=='请输入您的密码'){this.value='';this.style.color='#c1bfbf';}" />
	                    </li>
	                </ul>
	                <div class="pop_sumbit">
	                	<a href="/customer/findpass" id="customerfindPas" target="_blank" >个人找回密码</a>
	                	<a href="/company/findpass" id="companyfindPas" target="_blank" style="display: none">企业,管理员找回密码</a>
	                	<a href='/customer/register' id="customerRege" target="_blank">个人注册认证</a>
	                	<a href='/company/register' id="companyRege" target="_blank" style="display: none">企业注册认证</a>
	                    <input class="submit" type="button" id="loginButton" value="登&nbsp;录">
	                </div>
	            </form>
	        </div>
	        <div class="close" id="closeLoginDiv"><img src="/images/archives/pop_top.jpg" width="23" height="21"></div>
	    </div>
	    <div class="pop_up_bian"></div>
	</div>
	<div class="pop_up_bg"></div>
</div>
<script type="text/javascript">
uploadRootPath = "http://upload.11315.com";
host = window.location.host;
uploadCallbackURL = "?callback=http://"+host+"/"+"uploadCallback";
</script>
<script src="/js/lib/jQueryv1.10.2.js"></script>
<script src="/js/top.js?20160523"></script>
<script  type="text/javascript" src="/js/index.js?2017062101" ></script><script src="/js/kindeditor/kindeditor-min.js"></script>
<script src="/js/kindeditor/lang/zh_CN.js"></script>
<script src="/js/commmentBaseShow.js"></script>
<script src="/js/icp/login_icp.js"></script>

<script src="/js/pingfen/lib/jquery.raty.min.js"></script>
<script src="/js/icp/pingfen.js"></script>
<script src="/js/icp/v1v2Right.js"></script>
<script src="/js/icp/ranklistTop.js"></script>
<script type="text/javascript" src="/js/heightLine.js"></script>
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "//hm.baidu.com/hm.js?9aafda2b2c13a2bee5ddfdb4a72ca711";
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(hm, s);
})();
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

<script type="text/javascript">
   //右侧排行榜改成异步查询
   var isAjaxQueryTopCompany = $("#isAjaxQueryTopCompany").val();
   if("true"==isAjaxQueryTopCompany){
	   $("#topCompanyList").load("/ajaxGetTopCompanyList/"+$("#ajaxQueryTopCompanyId").val(), {
		    companyId : $("#ajaxQueryTopCompanyId").val()
		}).show();
   }

	// 上市公司信息展示
   if($(".listed_side_box").length > 0){
	   $(".listed_side_box").load("/ajaxGetListedCompanyInfo/"+$("#ajaxQueryTopCompanyId").val(), {
		    companyId : $("#ajaxQueryTopCompanyId").val()
		}).show();
	}
</script>
<script src="/js/showUserInfo.js"></script>
		<script src="/js/lib/formvalidate.js"></script>
<script src="/js/addComment.js?20160707"></script>
<script type="text/javascript">
	$('#acommentForm').kvvalidate();
	var unbindClickGotoPage = function(){
		$("#archivespinglun").find("a.gotoPage").attr("onClick", "");
	}
	unbindClickGotoPage();
//	$("#archivespinglun").on("click",".paginator a",function(){
	$("#archivespinglun").on("click",".page a",function(){
		var $this = $(this);
		var url=$this.attr("href");
		if(url && !$this.hasClass("gotoPage")){
			$("#archivespinglun").load(url,{},unbindClickGotoPage());
			$("html,body").animate({ scrollTop : $("#archivespinglun").offset().top-60 },"fast");
		}
		return false;
	});
	$("#archivespinglun").on("click","a.gotoPage",function(){
		var pageUrl = $(this).attr("pageUrl");
		var totalPage=parseInt("");
		var pageNumGo = $("#pageNumGo").val();
		if(""==pageNumGo){
			alert("请输入页码！");
		}else{
			if (/^\d+$/.test(pageNumGo)) {
     			if(pageNumGo>totalPage){
     				alert("超出最大页码");
     			} else{
     				var url=pageUrl+pageNumGo;
					$("#archivespinglun").load(url,{},unbindClickGotoPage());
					$("html,body").animate({ scrollTop : $("#archivespinglun").offset().top-60 },"fast");
     			}
			} else {
				alert("请输入数字！");
			}
		}

		return false;
	});
</script><!--查看地图-样式-->
<style type="text/css">
		html{height:100%}
		body{height:100%;margin:0px;padding:0px}
		#mapcontainer{position:fixed;margin: 0;padding: 0; z-index: 100000;display: none;top:105px; left:540px;_position:absolute;_top:630px;}
		#container{height:400px;width: 800px;position:absolute; top:0; border-radius:5px; border: 10px solid rgba(0,0,0,0.3);*border:#888 10px solid; background:none !important;}
		.anchorTR{top:25px !important; right:25px !important;}
</style>

	    <script type="text/javascript">
			var address = "杭州市滨江区网商路699号1号楼5楼";
			var lng = "";var lat = "";
			if((lng && lat) || address){
				var initmap = false;
				var marked = false;
				var initmapFun = function(){
					var map = new BMap.Map("container");
					map.enableScrollWheelZoom(true);
					map.addControl(new BMap.NavigationControl());
					map.addControl(new BMap.ScaleControl());
					map.addControl(new BMap.OverviewMapControl());
					map.addControl(new BMap.MapTypeControl());
					map.addControl(new BMap.OverviewMapControl({ isOpen: true, anchor: BMAP_ANCHOR_BOTTOM_RIGHT }));

					if(lng && lat){
						var point = new BMap.Point(lng, lat);
						var marker = new BMap.Marker(point);
				        map.addOverlay(marker);
				        var content = "杭州阿里巴巴广告有限公司" + "<br/><br/>地址：杭州市滨江区网商路699号1号楼5楼";
				        var label = new BMap.Label("杭州阿里巴巴广告有限公司",{offset:new BMap.Size(20,-10)});
				        marker.setLabel(label);
				        var infoWindow = new BMap.InfoWindow("<p style='font-size:14px;'>" + content + "</p>");
				        marker.addEventListener("click", function () { this.openInfoWindow(infoWindow); });
				        marked = true;
				        markercomp = marker;
						map.centerAndZoom(point, 13);
					}else {
						map.centerAndZoom("浙江省杭州市滨江区", 13);
						if(address){
							var localSearch = new BMap.LocalSearch(map);
							localSearch.enableAutoViewport();
							localSearch.setSearchCompleteCallback(function (searchResult) {
						        var poi = searchResult.getPoi(0);
								if(poi && !marked){
							        map.centerAndZoom(poi.point, 13);
							        var marker = new BMap.Marker(new BMap.Point(poi.point.lng, poi.point.lat));
							        map.addOverlay(marker);
							        var content = "杭州阿里巴巴广告有限公司" + "<br/><br/>地址：杭州市滨江区网商路699号1号楼5楼";

							        var label = new BMap.Label("杭州阿里巴巴广告有限公司",{offset:new BMap.Size(20,-10)});
							        marker.setLabel(label);
							        var infoWindow = new BMap.InfoWindow("<p style='font-size:14px;'>" + content + "</p>");
							        marker.addEventListener("click", function () { this.openInfoWindow(infoWindow); });
							        marked = true;
								}

						    });
					    	localSearch.search("杭州市滨江区网商路699号1号楼5楼");
						}
					}
					initmap = true;
				}
				//$("#loginDiv").show();
				$(".maplink").click(function(){
					$("#mapcontainer").show();
					if(!initmap){
						var mcLeft = $(document).width()/2-400;
						$("#mapcontainer").css("left",mcLeft);
						initmapFun();
					}
				});
				$("#closemapcontainer").click(function(){
					$("#mapcontainer").hide();
				});

			}
		</script>
	    <script>
			$("div.bdsolid").hover(function(){
				$(this).css("backgroundColor","#f0f0f0");
		 	},function(){
			 	$(this).css("backgroundColor","#fff");
		 	});
		 	var company_tabs_len = $('.companyNews_tit').find('li').length;
		 	$('.companyNews_tit ul li').hover(function(){
			 	var id = this.id;
			 	var sub = id.substr(-1);
				$('.companyNews_tit ul li').removeClass('active');
			 	$(this).addClass('active');
			 	$('.companyNews div').hide();
			 	$('#company_news_'+sub).show();
		 	});
		 	var initCount = function(){
	    		var companyId = $("#companyId").val();
		    	jQuery.getJSON("/getSdNsCount?companyId=" + companyId, function(json) {
		    		var result=json.split(",");
		    		var utilitiesCount = result[0];
		    		var ratepayingCount = result[1];
		    		var arrearCount = result[2];
		    		var total = parseInt(arrearCount)+parseInt(utilitiesCount);
		    		var arrearUrl="";
		    		var utilitiesUrl="";
		    		var arrearParam="";
		    		var utilitiesParam = "";
		    		if (arrearCount > 0) { //欠费
		    			arrearUrl="/acl/sd/%s/1";
		    			arrearParam = "target='_blank'";
					}else{
						arrearCount = "&nbsp;";
						arrearUrl="javascript:void(0)";
					}
		    		if (utilitiesCount > 0) { // 交费
		    			utilitiesUrl = "/acl/sd/%s/0";
		    			utilitiesParam = "target='_blank'";
					}else{
						utilitiesCount = "&nbsp;";
						utilitiesUrl="javascript:void(0)";
					}
		    		if(total > 0){
		    			var url =  utilitiesCount > 0 ? utilitiesUrl : arrearUrl ;
		    			$("#utilitiesh4").html('<p>共<a href="'+url+'" target="_blank">'+total+'</a>条信息（交费信息<a href="'+utilitiesUrl+'" '+utilitiesParam+'>'
		    			+ utilitiesCount
		    			+ '</a>条，欠费信息<a href="'+arrearUrl+'" '+arrearParam+'>'
		    			+ arrearCount
		    			+ '</a>条）</p><a href="'+url+'" target="_blank">6-3.水电气话费等费用信息</a>');
		    		} else {
		    			$("#utilitiesh4").html('<p>共<a href="javascript:void(0)">&nbsp;</a>条信息（交费信息<a href="'+utilitiesUrl+'">'
		    			+ utilitiesCount
		    			+ '</a>条，欠费信息<a href="'+arrearUrl+'">'
		    			+ arrearCount
		    			+ '</a>条）</p><a href="javascript:void(0)">6-3.水电气话费等费用信息</a>');
		    		}
		    		if(ratepayingCount > 0){
		    			$("#ratepayingh4").html('<p>共<a href="/acl/ns/%s/1" target="_blank">'
		    			+ ratepayingCount
		    			+ '</a>条信息</p><a href="/acl/ns/%s/1" target="_blank">6-4.纳税信息</a>');
		    		} else {
		    			$("#ratepayingh4").html('<p>共<a href="javascript:void(0)">&nbsp;</a>条信息</p><a href="javascript:void(0)">6-4.纳税信息</a>');
		    		}
				});

				jQuery.getJSON("/getTradeLendingCount?companyId=" + companyId, function(json) {
		    		var result=json.split(",");
		    		var goodNum = parseInt(result[0]);
		    		var badNum = parseInt(result[1]);
		    		var normalNum = parseInt(result[2]);
		    		var sumNum = goodNum + badNum + normalNum;
		    		var percent = '-';
		    		if(goodNum + badNum > 0){
		    			percent = goodNum/(goodNum + badNum);
		    			percent = (percent * 100).toFixed(1);
		    		}
		    		var htmlsrc = '';
		    		if(sumNum > 0){
		    			htmlsrc = htmlsrc + '<p style="width: 220px;"><span>良好率' + percent + '%</span>共<a href="/acl/tl/%s" target="_blank">' + sumNum + '</a>条信息 ';

		    			htmlsrc = htmlsrc + '</p>';
		    			htmlsrc = htmlsrc + '<a href="/acl/tl/%s" target="_blank">5-1.商业银行信贷评价信息</a><span class="span_special">（请向中国人民银行征信中心查询）</span>';
		    		} else {
		    			htmlsrc = htmlsrc + '<p style="width: 220px;"><span>良好率-%</span>共<a href="javascript:void(0)">&nbsp;</a>条信息 '
		    				+ '</p><a href="javascript:void(0)">5-1.商业银行信贷评价信息</a><span class="span_special">（请向中国人民银行征信中心查询）</span>';
		    		}
		    		$("#tradeLendingh4").html(htmlsrc);
				});

				//查看是有“和谐劳动关系示范企业”称号
				jQuery.getJSON("/getharmoniouslaborcompany?companyId=" + companyId, function(json) {
					var result=json.split(",");
					var countNum = result[0];
					var scoreId = result[1];
					var html='';
					if(countNum > 0){
						//$("#harmoniousLabor").attr("style","display:none");
// 						html+='<p>共<a href="/acl/al/'+companyId+'">'+countNum+'</a>条信息</p>'
// 						html+='<a href="/acl/al/'+companyId+'" target="_blank">6-5.劳动关系示范企业</a>';
						html+='<li style="width:132px">和谐劳动关系（<a href="/acl/s/'+companyId+'?scoreId='+scoreId+'" target="_blank">'+countNum+'</a>条）</li>'
					}
					$(".v1-business ul").append(html);;
				});
			};
			initCount();
			$(".qualioverdue").hover(function(){
			$(this).fadeTo("slow", 0);
			},function(){
			$(this).fadeTo("slow", 0.6);
			});
			$("img").not(".tdcodeimg").bind("contextmenu",function(){return false;});
			$(".con-table td").not(".comppname").bind("copy cut",function(){return false;});
			$(".con-table td").not(".comppname").bind("selectstart",function(){return false;});
		</script>
		<div style="display:none;"><script src="http://float2006.tq.cn/floatcard?adminid=9266912&sort=0"></script></div>
<script>
function dealAlltqCookie(){
	var strCookie=document.cookie;
	var arrCookie=strCookie.split(";");
	for(var i=0;i<arrCookie.length;i++){
		var arr=arrCookie[i].split("=");

		var name = arr[0];
		var cookievalue=arr[1];
		if (/^.*[\u4e00-\u9fa5]+.*$/.test(cookievalue)){
		 	var exp = new Date();
		 	exp.setTime(exp.getTime() + 24*3600*1000);
		 	document.cookie= name + "="+escape(cookievalue)+";expires="+exp.toGMTString();
		}
	}
}
dealAlltqCookie();
</script><script src="http://admin.11315.com:8089/accstaticis/rec"></script>
		<script type="text/javascript"src="/js/lib/toolTip.js"></script>
		<script type="text/javascript"src="/js/lib/jquery.lazyload.min.js"></script>
        <script type="text/javascript">
			$(".imgdiv").hover(
				function() {
					toolTip("<img src='"+ $(this).attr("source") + "'/>");
				}, function() {
					toolTip();
				});
			$("img.lazy").lazyload({
			    effect : "fadeIn"
			});
		</script>
		<script type="text/javascript">
		var commentGoodPercent1 = '0.0',commentGoodPercent2 = '-',
		commentGoodPercent3 = '-',commentGoodPercent6 = '-',ctxPath = '';
		</script>
		</body>
</html>
"""


class Parser:
    def parse_url(self, tree):
        company_name = self.parse_html_label(
            tree, '//*[@id="main"]/div/div[1]/div[1]/div[2]/table//tr[1]/th[2]/text()')

        principal_url = None
        style = self.parse_html_label(tree, '//*[@id="main"]/div/div[1]/div[1]/div[2]/table//tr[4]/td/p/@style')
        if style:
            principal_url = re.search(r'(http:.*?\.jpg)', style).group(1)

        phone_url = None
        style = self.parse_html_label(tree, '//*[@id="main"]/div/div[1]/div[1]/div[2]/table//tr[6]/td[1]/p/@style')
        if style:
            phone_url = re.search(r'(http:.*?\.jpg)', style).group(1)

        trade = self.parse_html_label(tree, '//*[@id="main"]/div/div[1]/div[1]/div[2]/table//tr[5]/td/text()')
        trade_url = self.parse_html_label(tree, '//*[@id="main"]/div/div[1]/div[1]/div[2]/table//tr[7]/td[2]/a/@href')
        location = self.parse_html_label(tree, '//*[@id="main"]/div/div[1]/div[1]/div[2]/table//tr[7]/td[1]/text()')
        detail_address = self.parse_html_label(tree, '//*[@id="main"]/div/div[1]/div[1]/div[2]/table//tr[8]/td/text()')
        main_product = None
        style = self.parse_html_label(tree, '//*[@id="main"]/div/div[1]/div[1]/div[2]/table//tr[9]/td/p/@style')
        if style:
            main_product = re.search(r'(http:.*?\.jpg)', style).group(1)
        company_introduce = self.parse_html_label(tree,
                                                  '//*[@id="main"]/div/div[1]/div[1]/div[2]/table//tr[10]/td/text()')

        base_information_url = '/cil/index/%s'
        shareholder_information_url = '/cil/gdl/%s'
        change_information_url = '/cil/bgl/%s'
        principle_members_url = '/cil/kp/%s'
        branch_information_url = '/cil/org/%s'
        equity_pledged_url = '/cil/stockEqu/%s'
        chattel_mortgage_url = '/cil/chatList/%s'
        check_information_url = '/cil/ccjcl/%s'
        clearing_information_url = '/cil/clear/%s'
        commerce_punishment_url = '/cil/xzcfgsl/%s'
        other_punishment_url = '/cil/xzcfqtl/%s'
        business_anomaly_url = '/cil/jyycl/%s'
        illegal_information_url = '/cil/yzwfl/%s'
        competent_department = '/cil/zhgbm/%s'
        enterprise_annual = '/cil/annualjiben/%s'
        administrative_licensing_url = '/acl/qf/%s/1'
        administrative_penalty_url = '/acl/am/%s/1'
        discriminative_information_url = '/acl/v/%s/1'
        guild_information_url = '/acl/as/%s/1'

        return (
            company_name, principal_url, phone_url, trade, trade_url, location, detail_address, main_product,
            company_introduce,
            base_information_url, shareholder_information_url, change_information_url, principle_members_url,
            branch_information_url, equity_pledged_url, chattel_mortgage_url, check_information_url,
            clearing_information_url, commerce_punishment_url, other_punishment_url, business_anomaly_url,
            illegal_information_url, competent_department, enterprise_annual, administrative_licensing_url,
            administrative_penalty_url, discriminative_information_url, guild_information_url,
        )

    @staticmethod
    def parse_html_label(html_label, xpath):
        item = html_label.xpath(xpath)
        if item:
            item = item[0].strip().replace('\xa0', '').replace('\n', '')
        return item


p = Parser()
tree = etree.HTML(content_string)
item = p.parse_url(tree)
print(item)
# r = re.search(r'\d{13}', content_string).group()
# print(r)
# '//*[@id="main"]/div/div[1]/div[1]/div[2]/table//tr[7]/td[2]/a/@href'
# '//*[@id="main"]/div/div[1]/div[1]/div[2]/table//tr[1]/th[2]/@title'
#
# company_name = tree.xpath('//*[@id="main"]/div/div[1]/div[1]/div[3]//p/a[1]/@href')

''
# print(company_name)
