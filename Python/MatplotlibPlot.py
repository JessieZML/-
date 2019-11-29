"""
一些设置
"""
sns.set_style("darkgrid")
# 显示中文
plt.rcParams["font.family"] = "SimHei"
# 正常显示字符
plt.rcParams["axes.unicode_minus"]
# 设置线条样式
plt.rcParams["font.size"] = 15


"""
子图设置
"""
# 超越常规网格到跨越多行和列的子图plt.GridSpec()是最好的工具。
# 该plt.GridSpec()对象本身不会创建一个图; 
# 它只是一个方便的界面，可以被plt.subplot()命令识别。
# 例如，具有一些指定宽度和高度空间的两行和三列网格的gridspec：

grid = plt.GridSpec(2, 3, wspace=0.4, hspace=0.3)
# 从这里我们可以使用familiary Python切片语法指定子图位置和范围：

plt.subplot(grid[0, 0])
plt.subplot(grid[0, 1:])
plt.subplot(grid[1, :2])
plt.subplot(grid[1, 2]);


"""
流量计画图相关
"""
class MatplotlibPlot()：
    """ 工作中常用的matplotlib画图代码"""
    
    def corr_plot(data, attr1, attr2, ids, date1, date2, minites=60, fmt='%H:%M', exp=False, exp_path='./picture/ids.png'):
        """ 两个字段之间相关性画图
        
        生成三张图，左侧两图为短时间内的数据随时间变化折线图，右侧图为两个字段之间的散点图，以及用一元线性回归生成的回归直线。
        
        参数
        ----------
        data : DataFrame
        
        attr1 : string
            X轴字段名
        
        attr2 : string
            y轴字段名
        
        ids : int
            当前设备id
        
        date1 : string
            左侧两折线图的起始画图时间
        
        date2 : string
            左侧两折线图的结束画图时间
        
        minites : int, optional, default 60
            左侧两折线图的x轴时间间隔设置
        
        fmt : string, optional, default '%H:%M'
            左侧两折线图的x轴显示格式
        
        exp : boolean, optional, default False
            是否要将图片另存为文件
        
        exp_path : string, optional, default './picture/ids.png'
            文件路径

        示例
        ----------
        
        >>> corr_plot(data, 'InstantaneousFlow', 'Current', 6361, '2019-09-13 00:00:00', '2019-09-14 00:00:00', minites=60, exp=False)
        >>> 
        
        """
        %matplotlib inline
        sns.set(style="darkgrid", palette="muted", color_codes=True)
        df = data[date1:date2].copy()
        date = date1.split(' ')[0]

        fig = plt.figure(figsize=(22, 7))
        G = gridspec.GridSpec(2, 2, width_ratios=[1.5, 1])

        ax0 = plt.subplot(G[0, 0])
        ax0.plot(df.index, df[attr1], label=attr1)
        ax0.set_ylabel(attr1, fontsize=14)
        ax0.legend(fontsize=14)
        ax0.xaxis.set_major_formatter(mdates.DateFormatter(fmt))  # 设置时间标签显示格式
        locator = mdates.AutoDateLocator()
        locator.intervald[MINUTELY] = [minites]  # only show every 1 minutes
        ax0.get_xaxis().set_major_locator(locator)
        ax0.tick_params(labelsize=14)

        ax1 = plt.subplot(G[1, 0])
        ax1.plot(df.index, df[attr2], label=attr2)
        ax1.set_ylabel(attr2, fontsize=14)
        ax1.set_xlabel('Date: %s' % date, fontsize=14)
        ax1.legend(fontsize=14)
        ax1.xaxis.set_major_formatter(mdates.DateFormatter(fmt))  # 设置时间标签显示格式
        locator = mdates.AutoDateLocator()
        locator.intervald[MINUTELY] = [minites]  # only show every 1 minutes
        ax1.get_xaxis().set_major_locator(locator)
        ax1.tick_params(labelsize=14)

        from sklearn.linear_model import LinearRegression
        corr = data[[attr1, attr2]].copy()
        corr.sort_values(by=attr1, inplace=True)
        corr.dropna(inplace=True)
        X = np.array(corr[attr1]).reshape(-1, 1)
        y = np.array(corr[attr2]).reshape(-1, 1)
        lr = LinearRegression()
        lr.fit(X, y)
        yr = lr.predict(X)

        ax2 = plt.subplot(G[:, 1])
        ax2.scatter(X, y, alpha=0.6)
        ax2.plot(X, yr, c='r', linewidth=2, label='y = %.4f + %.4f * x' %
                 (lr.intercept_, lr.coef_))
        ax2.set_xlabel(attr1, fontsize=14)
        ax2.set_ylabel(attr2, fontsize=14)
        ax2.tick_params(labelsize=14)
        ax2.legend(fontsize=15)

        plt.suptitle('Id: %u   Corr: %.4f' %
                     (ids, corr.corr().iloc[0, 1]), fontsize=17)
    #     print(r'pre = %.4f + %.4f * InstantaneousFlow' %
    #           (lr.intercept_, lr.coef_))

        if exp:
            fig = plt.gcf()
            fig.savefig(exp_path)
        
        plt.show()
        
        return lr.intercept_, lr.coef_, corr.corr().iloc[0, 1]    
