# 百度搜索访问python官网
# 柱状 饼状 雷达图
from pyecharts import options as opts
from pyecharts.charts import Bar

c = (
    Bar()
    .add_xaxis(
        [
            "1月",
            "2月",
            "3月",
            "4月",
            "5月",
            "6月",
            "7月",
            "8月",
            "9月",
            "10月",
            "11月",
            "12月",
        ]
    )
    .add_yaxis("重庆", [10, 20, 30, 40, 50, 40, 50, 60, 80, 70, 40, 30])
    .add_yaxis("天津", [10, 20, 30, 40, 50, 40, 50, 60, 80, 70, 40, 30])
    .add_yaxis("北京", [10, 20, 30, 40, 50, 40, 50, 60, 80, 70, 40, 30])
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
        title_opts=opts.TitleOpts(title="中国某三地降水量", subtitle="解决标签名字过长的问题"),
    )
    .render("bar_rotate_xaxis_label.html")
)
import webbrowser

webbrowser.open("bar_rotate_xaxis_label.html")
