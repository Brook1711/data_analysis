# 放大转发（AF）和解码转发

## 放大转发(AF)

在AF模式下，中继节点对收到的数据不进行任何的解调或解码操作，只对信号的功率作归一化处理，然后用自身的发射功率将信号放大后发射给目的节点。
AF方式：操作简单，开销小，复杂度低，但在放大有用信号的同时也放大了噪声，在信道状况较差时并不能获得良好的性能。
中继节点不对接收的信号进行解调和解码，而是直接将收到的信号进行模拟处理后转发，这是采用最早的一种协作模式。 在该机制中，每个用户接收它伙伴发送过来的带有噪声的信号，接着对该信号进行放大，然后将放大的带有噪声信号重新发送。基站将对用户和其伙伴传送来的数据进行合并判决。 尽管协作者在进行放大时也放大了噪声，但是基站接收到两个独立的衰落信号，最后能作出较好的判决。

## 解码转发（DF)decode-forward

在DF模式下，中继节点对用户的信息进行解调，解码之后仍用原来的编码方式进行编码，然后发送给目的节点。通过循环冗余校验来判断是否收到正确的数据包，如果无误则进行转发，如果有误则将其丢弃。
DF方式：通过对数据先进行解调解码从而将源节点与中继节点之间的噪声剔除掉，同时利用循环冗余校验(CRC）避免了错误信息的扩散，但是会降低频谱效率，丢弃数据包也会损失一定的能量，造成接收端信噪比的下降。因此比较适合信道状况较好时使用。
AF和DF方式都是对信息的重复传输。
DF方式不会带来噪声传播的问题，但是如果不采用CRC循环冗余校验，则得不到满分集阶数。并且中继节点对源节点信息解码错误所带来的的误差会随着跳数（经历的中继节点的个数）的增加而产生累积。


# activate RIS技术相对AF和DF

RIS在物理层信道层面对信道矩阵进行直接编程，而AF和DF直接引入了新的无线电发射源

1、时延

RIS在反射信号时并不获取信号，直接对信号进行反射，多径干扰*rms*时延扩展可以通过编程手段控制。

2、直连链路

多数AF和DF的模型假设中发送端和接收端的直连链路被直接遮挡，但是activate RIS可以通过对反射面进行编程形成波束赋形对原有直连链路信号进行增强。

3、功耗

active RIS虽然引入了新的射频链路，但是根据N平方律增长率，可以通过增加RIS反射元数量来增强信号，所以其功耗一定会比AF和DF小

4、同频干扰

AF和DF直接引入了新的无线电发射源，在蜂窝移动通信和超密集组网场景下会引入新的同频干扰问题，但是active RIS可以通过更高能效的发射功耗和更细粒度的反射波束赋形来削弱同频干扰。