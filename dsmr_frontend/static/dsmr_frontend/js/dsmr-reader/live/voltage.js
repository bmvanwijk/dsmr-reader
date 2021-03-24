$(document).ready(function () {
    let echarts_voltage_graph = echarts.init(document.getElementById('echarts-voltage-graph'));
    let echarts_voltage_initial_options = {
        toolbox: TOOLBOX_OPTIONS,
        color: [
            VOLTAGE_L1_COLOR,
            VOLTAGE_L2_COLOR,
            VOLTAGE_L3_COLOR
        ],
        title: {
            text: TEXT_VOLTAGE_HEADER,
            textStyle: TITLE_TEXTSTYLE_OPTIONS,
            left: 'center',
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow',
                label: {
                    show: true
                }
            }
        },
        calculable: true,
        grid: {
            top: '12%',
            left: '1%',
            right: '2%',
            containLabel: true
        },
        xAxis: [
            {
                type: 'category',
                boundaryGap: false,
                data: null
            }
        ],
        yAxis: [
            {
                type: 'value',
                min: 'dataMin',
                max: 'dataMax'
            }
        ],
        dataZoom: [
            {
                show: true,
                start: LIVE_GRAPHS_INITIAL_ZOOM,
                end: 100
            },
            {
                type: 'inside',
                start: 0,
                end: 100
            }
        ],
    };

    /* These settings should not affect the updates and reset the zoom on each update. */
    let echarts_voltage_update_options = {
        xAxis: [
            {
                type: 'category',
                boundaryGap: false,
                data: null
            }
        ],
        series: null
    };

    echarts_voltage_graph.showLoading('default', ECHARTS_LOADING_OPTIONS);

    /* Init graph. */
    $.get(ECHARTS_VOLTAGE_GRAPH_URL, function (xhr_data) {
        echarts_voltage_graph.hideLoading();

        /* Dynamic phases. */
        if (IS_MULTI_PHASE) {
            echarts_voltage_update_options.series = [
                {
                    name: 'L1',
                    type: 'line',
                    data: null
                },
                {
                    name: 'L2',
                    type: 'line',
                    data: null
                },
                {
                    name: 'L3',
                    type: 'line',
                    data: null
                },
            ];
        } else {
            echarts_voltage_update_options.series = [
                {
                    name: 'Volt',
                    type: 'line',
                    data: null
                }
            ];
        }

        echarts_voltage_graph.setOption(echarts_voltage_initial_options);

        /* Different set of options, to prevent the dataZoom being reset on each update. */
        echarts_voltage_update_options.xAxis[0].data = xhr_data.read_at;
        echarts_voltage_update_options.series[0].data = xhr_data.phase_voltage.l1;

        if (IS_MULTI_PHASE) {
            echarts_voltage_update_options.series[1].data = xhr_data.phase_voltage.l2;
            echarts_voltage_update_options.series[2].data = xhr_data.phase_voltage.l3;
        }

        echarts_voltage_graph.setOption(echarts_voltage_update_options);


        // Schedule updates
        let latest_delta_id = xhr_data.latest_delta_id;
        let pending_xhr_request = null;

        setInterval(function(){
            // Do not send new XHR request update if the previous one is still pending.
            if (pending_xhr_request !== null) {
                return;
            }

            pending_xhr_request = $.ajax({
                dataType: "json",
                url: ECHARTS_VOLTAGE_GRAPH_URL + "&latest_delta_id=" + latest_delta_id,
            }).done(function(xhr_data) {
                /* Ignore empty sets. */
                if (xhr_data.read_at.length === 0) {
                    return;
                }

                /* Delta update. */
                for (let i = 0; i < xhr_data.read_at.length; i++) {
                    echarts_voltage_update_options.xAxis[0].data.push(xhr_data.read_at[i]);
                    echarts_voltage_update_options.series[0].data.push(xhr_data.phase_voltage.l1[i]);

                    if (IS_MULTI_PHASE) {
                        echarts_voltage_update_options.series[1].data.push(xhr_data.phase_voltage.l2[i]);
                        echarts_voltage_update_options.series[2].data.push(xhr_data.phase_voltage.l3[i]);
                    }
                }

                latest_delta_id = xhr_data.latest_delta_id;
                echarts_voltage_graph.setOption(echarts_voltage_update_options);
            }).always(function(){
                // Allow new updates
                pending_xhr_request = null;
            });
        }, ECHARTS_VOLTAGE_GRAPH_INTERVAL * 1000);
    });
});

$(window).resize(function () {
    echarts_voltage_graph?.resize();
});