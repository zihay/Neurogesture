function createChart(frequency, transition, elementById, title) {
    var myChart = echarts.init(document.getElementById(elementById));
    myChart.showLoading();
    myChart.hideLoading();
    fre = frequency
    trans = transition
    nodes = fre
    categories = ['camera', 'look_down', 'slide', 'look_away_slide', 'other']
    nodes = []
    for (var key in fre) {
        nodes.push({
            'id': key,
            'name': key,
            'value': fre[key]
        })
    }
    nodes.forEach(function(node) {
        categories.forEach(function(c, i) {
            if (node.name.includes(c)) {
                node.category = i
            }
        })
        node.itemStyle = null;
        node.symbolSize = node.value * 200 + 5;
        node.value = node.symbolSize;
        node.label = {
            normal: {
                show: true
            }
        };
    });
    trans = trans.filter(function(t) {
        if (t.prob == 0.0) {
            return false
        }
        return true
    })
    i = 0
    links = trans.map(function(t, i) {
        return {
            'id': i,
            'source': t.source,
            'target': t.target,
            'lineStyle': {
                'width': t.prob * 10
            }
        }
    })
    option = {
        title: {
            text: title,
            subtext: 'Circular layout',
            // top: 'bottom',
            // left: 'right'
        },
        legend: [{
            data: categories
        }],
        animationDurationUpdate: 1500,
        animationEasingUpdate: 'quinticInOut',
        series: [{
            name: title,
            type: 'graph',
            layout: 'circular',
            focusNodeAdjacency: true,
            circular: {
                rotateLabel: true
            },
            categories: categories.map(function(c) {
                return {
                    'name': c
                }
            }),
            edgeSymbol: ['circle', 'arrow'],
            data: nodes,
            links: links,
            roam: true,
            label: {
                normal: {
                    position: 'right',
                    formatter: '{b}'
                }
            },
            lineStyle: {
                normal: {
                    color: 'source',
                    curveness: 0.1
                }
            }
        }]
    };

    myChart.setOption(option);
}