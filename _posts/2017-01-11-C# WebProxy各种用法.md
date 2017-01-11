---
layout: post
title: .NET中代理服务器WebProxy的各种用法
date: 2017-01-11 
tags: 知识分享   
---
# .NET中代理服务器WebProxy的各种用法 #
[引用地址](http://blog.sina.com.cn/s/blog_58c506600101a3p7.html "引用地址")
>因为涉及到代理的各种情况，WebRequest和WebProxy类的文档写的相当复杂，不但各个文档关注点不同，而且不同版本的同一文档也有小小的区别，网上也没有关于这个类的相关文章。于是乎这篇Blog是我钻研半天MSDN很久后总结并且花了一小时憋出来的，希望下面的内容能帮到大家。
>AcDown中也使用了相关的代码，有兴趣的可以找来看看【解析】.NET中代理服务器WebProxy的各种用法）
> 
>直接进入正题，对于需要使用WebProxy类的情况，大致分如下几种：
>1、创建WebRequest的时候，没有刻意设置代理（默认情况）
>2、使用Internet Explorer代理
>3、使用应用程序配置文件中的代理
>4、不使用代理
>5、使用.NET框架默认设置的代理
>6、使用WPAD配置脚本自动设置的代理
>7、使用IE+应用程序配置文件的混合代理
>8、使用IE代理但禁用自动代理检测(WPAD)
>
>怎么样，很混乱吧。当然上面这些很多都是重复的，不过基本已经涵盖了所有可能遇到的情况，下面让我来一个一个说说：
>
>1、默认情况下的代理设置
>当创建一个新的HTTP请求时（WebRequest.Create方法），得到的HttpWebRequest类会自动初始化它的Proxy属性，那么这个属性的默认值是什么呢？MSDN中说：
> 
> 如果配置文件中未指定代理并且未指定 Proxy 属性，则 HttpWebRequest 类使用从本地计算机上的 Internet Explorer 中继承的代理设置。 如果 Internet Explorer 中没有代理设置，请求会直接发送到服务器。 
> 
>这段话中，说到Proxy属性使用的其实就是默认代理，这个默认代理默认来自于IE，如果IE没有设置代理，那么就会直接连接到目标服务器。为什么要说“默认代理默认来自于IE”呢？因为这个“默认来自于IE”也是可以修改的，通过修改WebProxy.DefaultWebProxy属性，你可以控制每次新建请求时所使用的默认代理：
> 
>DefaultWebProxy 属性从 app.config 文件中读取代理服务器设置。 如果没有配置文件，则使用当前用户的 Internet Explorer (IE) 代理设置。
>如果 DefaultWebProxy 属性设置为 null，则使用 Create 或 CreateDefault 方法创建的 WebRequest 类的所有后续实例都没有代理。
>这里需要注意的是，如果DefaultWebProxy设置为null，并不意味着WebRequest的Proxy属性也是null，这两个null表示的意义不同。
> 
> 
>2、使用IE代理，但不使用任何动态设置
>最简单的方法是将Proxy属性设置为WebProxy.GetDefaultProxy，GetDefaultProxy会读取当前计算机上的IE代理设置，同时忽略掉所有动态设置的内容：
>GetDefaultProxy 方法读取 Internet Explorer 5.5 和更高版本存储的非动态代理设置并使用这些设置创建 WebProxy 实例。
>GetDefaultProxy 方法不获取从 Internet Explorer 运行的脚本、从自动配置项或者从 DHCP 或 DNS 查找生成的任何动态设置。
>但是这个API已经过时，所以现在我推荐的方法是：将Proxy属性设置为null：
>http://msdn.microsoft.com/zh-cn/library/fze2ytx2(v=vs.80).aspx
>
>
>3、使用IE代理，同时使用各种动态配置项
>这个是比较简单的了，当然这种情况还是会包含两种小的情况：
>(1)使用app.config中的配置：将Proxy属性设置为 WebProxy.DefaultWebProxy 
>(2)不使用app.config中的配置：将Proxy属性设置为 WebRequest.GetSystemWebProxy()
>GetSystemWebProxy 方法读取当前用户的 Internet Explorer (IE) 代理设置。 此进程包括 IE 选项来自动检测代理设置，请使用自动配置脚本、手动代理服务器设置和高级手动代理服务器设置。 
>
>
>4、不使用任何代理
>不使用任何代理的方法是：创建一个WebProxy类的新实例：
>默认构造函数通过将 Address 属性设置为 null 来初始化 WebProxy 类的空实例。
>Address 属性为 null 时，IsBypassed 方法返回 true，且 GetProxy 方法返回目标地址。
>另外再来看看Address属性的说明：
>Address 属性包含代理服务器的地址。 如果未启用自动代理检测并且未指定自动配置脚本，则 Address 属性与 BypassList 共同确定用于请求的代理。
>当 Address 属性为 null 时，请求回避此代理并且直接连接到目标主机。
>综上所述，也就是说，当使用无参构造函数创建一个新的WebProxy对象时（req.Proxy = new WebProxy();），这个请求会绕过所有代理服务器直接连接目标服务器。
>
>
>5、其他
>关于如何设置app.config/machine.config配置文件中的代理设置：
><defaultProxy>元素：http://msdn.microsoft.com/zh-cn/library/kd3cf2ex
><proxy>元素：http://msdn.microsoft.com/zh-cn/library/sa91de1e(v=vs.100).aspx
