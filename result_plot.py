import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pymysql
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['STSong']    # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False           # 解决保存图像是负号'-'显示为方块的问题

def pie_plot():
    # connection = pymysql.connect(host='localhost',  # host属性
    #                              port=3306,
    #                              user='root',  # 用户名
    #                              password='mysql',  # 此处填登录数据库的密码
    #                              db='rdf_metadata',  # 数据库名
    #                              )
    # cur = connection.cursor()
    # sql = 'SELECT db_name, count(*) as cnt FROM summary_dataset GROUP BY db_name ORDER BY cnt DESC;'
    # cur.execute(sql)
    # results = cur.fetchall()
    # labels = [x[0] for x in results]
    # values = [x[1] for x in results]

    # 设置画布大小
    plt.figure(figsize=(10, 10))
    # 设置每块区域的标签
    labels = ['a', 'b', 'c', 'd', 'e']
    # 设置每块区域离圆心的距离，这里a区域凸出一点点
    explode = [0.05, 0.01, 0.01, 0.01, 0.01]
    # 设置每块区域的值
    values = [1, 5, 2, 4, 3]
    # 设置每块区域的颜色
    colors = ['#F5DEB3', '#87CEFA', '#FFB6C1', '#90EE90', '#D3D3D3']

    z = {'2': 11107, '4': 79, '3': 1433, '5': 25, '6 and larger': 72}
    labels = ['2', '3', '4', '5', '6 and larger']
    values = [z[x] for x in labels]

    _, l_text, p_text = plt.pie(values, explode=explode, labels=labels, autopct='%1.1f%%', colors=colors)

    # 设置标签字体大小
    for t in l_text:
        t.set_size(18)
    # 设置数值字体大小
    for t in p_text:
        t.set_size(18)

    # 标题
    plt.title(u'Title', fontsize=18)

    # 图例
    plt.legend(fontsize=18)

    # 保存图片
    # plt.savefig('./figure.pdf', bbox_inches='tight')
    # 显示图片
    plt.show()


def bar_plot():
    z = {'2': 1595, '3': 552, '4': 287, '5': 182, '6 and larger': 524}
    num = sum(z.values())
    for k, v in z.items():
        s = '            {} & {} & {:.2%} \\\\'.format(k, v, v/num)
        print(s.replace('%', '\\%'))
    z = [('data.medicaid.gov', 2926), ('data.gov', 2316), ('dati.gov.it', 1076), ('opendata.utah.gov', 937), ('data.winnipeg.ca', 563)]
    num = sum([2926, 2316, 1076, 937, 563, 372, 338, 271, 205, 178, 162, 161, 161, 151, 138, 118, 102, 99, 99, 95, 94, 92, 90, 74, 71, 69, 68, 67, 54, 53, 52, 51, 50, 45, 42, 42, 41, 40, 39, 38, 37, 37, 37, 34, 34, 34, 32, 32, 32, 30, 30, 29, 29, 28, 28, 28, 25, 24, 24, 22, 21, 20, 20, 20, 20, 18, 18, 18, 17, 17, 17, 16, 16, 15, 15, 15, 14, 13, 13, 13, 13, 13, 12, 12, 12, 11, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
              )

    for i in z:
        s = '            {} & {} & {:.2%} \\\\'.format(i[0], i[1], i[1]/num)
        print(s.replace('%', '\\%'))
    for i in z:
        print(i[0], end='、')
    z = [0.5863384503587974, 0.1516032337178672, 0.0727586520119902, 0.0399672994822418, 0.14933236442910347]
    plt.bar(range(len(z)), z)
    plt.xticks([])
    plt.show()


def log_fit(x, y):
    """line fitting on log-log scale"""
    xx = np.nonzero(y)[0][1:]
    yy = np.array(y)[xx]
    k, m = np.polyfit(np.log(xx), np.log(yy), 1)
    print('k, m: ', k, m)
    x = np.array(x)
    return np.exp(m) * x ** (k)


def degree_plot():
    degree = [25353, 50192, 13673, 6571, 3983, 1803, 1511, 1216, 882, 477, 541, 497, 572, 247, 236, 195, 301, 168, 186, 138, 189, 65, 149, 44, 90, 89, 23, 71, 35, 135, 1420, 42, 16, 8, 12, 4, 25, 55, 19, 8, 48, 39, 4, 44, 6, 5, 7, 4, 6, 5, 5, 3, 5, 3, 1, 34, 17, 15, 1, 33, 4, 2, 0, 0, 2, 1, 9, 5, 3, 1, 0, 2, 2, 1, 1, 3, 1, 0, 2, 1, 0, 1, 37, 2, 4, 10, 1, 13, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 22, 1, 1, 0, 0, 1, 1, 1, 1, 0, 2, 5, 6, 3, 4, 1, 1, 2, 1, 1, 0, 0, 3, 2, 2, 0, 0, 2, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 734, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    print(degree)
    temp = degree[200:]
    print(degree.index(734))
    print(max(temp), temp.index(max(temp)))
    print('max degree:', len(degree))
    x = range(len(degree))  # 生成x轴序列，从1到最大度
    y = [z / float(sum(degree)) for z in degree]
    print(y)
    ys = log_fit(x[:200], y[:30])
    plt.loglog(x, y, '.')  # 在双对坐标轴上绘制度分布曲线
    plt.plot(x[:200], ys, label=r'$\gamma$=2.076')
    font1 = {'family': 'STSong',
            # 'family': 'Times New Roman',
             'weight': 'normal',
             'size': 11,
             }
    plt.xlabel('度（对数坐标）', font1)
    plt.ylabel('度分布（对数坐标） ', font1)
    plt.legend()
    plt.savefig('figure/degree-distribution2.pdf', bbox_inches='tight')
    plt.show()  # 显示图表


def csv_plot():
    df = pd.read_csv('figure/dataset-triples.csv')
    x = df['dataset_id'].to_list()
    y = df['cnt'].to_list()

    # y = [2926, 2316, 1076, 937, 563, 372, 338, 271, 205, 178, 162, 161, 161, 151, 138, 118, 102, 99, 99, 95, 94, 92, 90, 74, 71, 69, 68, 67, 54, 53, 52, 51, 50, 45, 42, 42, 41, 40, 39, 38, 37, 37, 37, 34, 34, 34, 32, 32, 32, 30, 30, 29, 29, 28, 28, 28, 25, 24, 24, 22, 21, 20, 20, 20, 20, 18, 18, 18, 17, 17, 17, 16, 16, 15, 15, 15, 14, 13, 13, 13, 13, 13, 12, 12, 12, 11, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    x = list(range(len(y)))
    print(len(x))

    plt.bar(x, y)
    # plt.plot(x, y, '.')
    font1 = {'family': 'STSong',
            # 'family': 'Times New Roman',
             'weight': 'normal',
             'size': 11,
             }
    plt.xlabel('数据集 ', font1)
    plt.ylabel('三元组数量（对数坐标）', font1)

    # my_x_ticks = np.arange(0, 400, 50)  # 原始数据有13个点，故此处为设置从0开始，间隔为1
    # plt.xticks(my_x_ticks)

    plt.yscale('log')
    # plt.xscale('log')
    plt.savefig('figure/datasets-rdf2.pdf', bbox_inches='tight')

    ax = plt.gca()

    plt.show()


if __name__ == '__main__':
    csv_plot()

