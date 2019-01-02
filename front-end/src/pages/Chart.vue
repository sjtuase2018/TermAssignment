<template>
  <div>
    <v-container grid-list-md text-xs-center>
      <template>
        <v-layout row wrap>
          <v-flex xs16 sm8 md4 offset-xs2>
            <v-menu ref="menuS" :close-on-content-click="false" v-model="menuS" :nudge-right="40" 
              lazy transition="scale-transition" offset-y full-width min-width="290px">
              <v-text-field slot="activator" v-model="startTime" label="开始日期" prepend-icon="event" readonly></v-text-field>
              <v-date-picker v-model="startTime" no-title scrollable></v-date-picker>
            </v-menu>
          </v-flex>
          <v-spacer></v-spacer>
          <v-flex xs16 sm8 md4>
            <v-menu ref="menuE" :close-on-content-click="false" v-model="menuE" :nudge-right="40" 
              lazy transition="scale-transition" offset-y full-width min-width="290px">
              <v-text-field slot="activator" v-model="endTime" label="终止日期" prepend-icon="event" readonly></v-text-field>
              <v-date-picker v-model="endTime" no-title scrollable></v-date-picker>
            </v-menu>
          </v-flex>
          <v-spacer></v-spacer>
          <v-flex xs16>
            <v-btn icon @click="getChart">
              <v-icon large>search</v-icon>
            </v-btn>         
          </v-flex>
          <v-spacer></v-spacer>
        </v-layout>
      </template>
      <v-layout row wrap>
        <v-flex>
          <div id="myChartWeek" :style="{width: '400px', height: '400px'}"></div>
        </v-flex>
        <v-flex>
          <div id="myChartArea" :style="{width: '400px', height: '400px'}"></div>
        </v-flex>
        <v-flex xs12>
          <div id="myChartMoon" :style="{width: '860px', height: '400px'}"></div>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {

    data() {
      return {
        startTime: '2018-1-1',
        endTime: '2019-1-1',
        menuS: false,
        menuE: false,
        dataWeek: [],
        dataMoon: {
          dataM1: [],
          dataM2: [],
          dataM3: [],
        },
        dataArea: {
          legendData: [],
          // legendData: ['地区1', '地区2', '地区3'],
          // selected: [{name: '地区1', value: 10},{name: '地区2', value: 10},{name: '地区3', value: 10},],
          seriesData: []
          // {
          //   name: '地区1',
          //   value: 10
          // }, {
          //   name: '地区2',
          //   value: 10
          // }, {
          //   name: '地区3',
          //   value: 10
          // }
        }
      }
    },
    mounted() {
      // console.log(this.dataWeek)
      const path = `http://localhost:5000/api/getChart/`;
      axios.post(path, {
          startTime: this.startTime,
          endTime: this.endTime
        }).then(response => {
          this.dataWeek = response.data.dataWeek,
            this.dataMoon.dataM1 = response.data.dataM1,
            this.dataMoon.dataM2 = response.data.dataM2,
            this.dataMoon.dataM3 = response.data.dataM3,
            this.dataArea.legendData = response.data.name;
          this.dataArea.seriesData = response.data.seriesData;

          this.drawLine();
        })
        .catch(error => {
          console.log(error)
        })

      // this.drawLine();
    },

    created() {
      this.endTime.date +=1;
      // const path = `http://localhost:5000/api/getChart/`;
      // axios.get(path).then(response => {
      //     console.log(response.data)
      //     console.log(response.data.dataWeek)
      //     console.log(this.dataWeek)
      //     this.dataWeek.push(response.data.dataWeek),

      //     console.log(this.dataWeek)
      //     this.dataMoon.dataM1 =response.data.dataM1,
      //     this.dataMoon.dataM2 =response.data.dataM2,
      //     this.dataMoon.dataM3 =response.data.dataM3
      //   })
      //   .catch(error => {
      //     console.log(error)
      //   })
    },
    methods: {
      getChart() {
        const path = `http://localhost:5000/api/getChart/`;
        axios.post(path, {
            startTime: this.startTime,
            endTime: this.endTime
          }).then(response => {
            this.dataWeek = response.data.dataWeek,
              this.dataMoon.dataM1 = response.data.dataM1,
              this.dataMoon.dataM2 = response.data.dataM2,
              this.dataMoon.dataM3 = response.data.dataM3,
              this.dataArea.legendData = response.data.name;
            this.dataArea.seriesData = response.data.seriesData;

            this.drawLine();
          })
          .catch(error => {
            console.log(error)
          })
      },

      drawLine() {
        //myChartWeek
        // 基于准备好的dom，初始化echarts实例
        let myChartWeek = this.$echarts.init(document.getElementById('myChartWeek'), 'dark')
        // 绘制图表
        myChartWeek.setOption({
          title: {
            text: '周数量统计',
          },
          xAxis: {
            type: 'category',
            data: ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
          },
          yAxis: {
            type: 'value'
          },
          series: [{
            data: this.dataWeek,
            type: 'line'
          }]
        });

        //myChartArea
        let myChartArea = this.$echarts.init(document.getElementById('myChartArea'), 'dark')
        // 绘制图表
        myChartArea.setOption({
          title: {
            text: '地区数量统计',
            x: 'center'
          },
          tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
          },
          legend: {
            type: 'scroll',
            orient: 'vertical',
            right: 10,
            top: 20,
            bottom: 20,
            data: this.dataArea.legendData,

            //selected: this.dataA.selected
          },
          series: [{
            name: '地区',
            type: 'pie',
            radius: '55%',
            center: ['40%', '50%'],
            data: this.dataArea.seriesData,
            itemStyle: {
              emphasis: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }]
        });

        //myChartMoon
        let myChartMoon = this.$echarts.init(document.getElementById('myChartMoon'), 'dark')
        myChartMoon.setOption({
          title: {
            text: '月数量统计',
          },
          tooltip: {
            trigger: 'axis'
          },
          legend: {
            data: ['无人区', '安全帽']
          },
          toolbox: {
            show: true,
            feature: {
              dataView: {
                show: true,
                readOnly: false
              },
              magicType: {
                show: true,
                type: ['line', 'bar']
              },
              restore: {
                show: true
              },
              saveAsImage: {
                show: true
              }
            }
          },
          calculable: true,
          xAxis: [{
            type: 'category',
            data: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
          }],
          yAxis: [{
            type: 'value'
          }],
          series: [{
              name: '无人区',
              type: 'bar',
              data: this.dataMoon.dataM1,
              markPoint: {
                data: [{
                    type: 'max',
                    name: '最大值'
                  },
                  {
                    type: 'min',
                    name: '最小值'
                  }
                ]
              },
              markLine: {
                data: [{
                  type: 'average',
                  name: '平均值'
                }]
              }
            },
            {
              name: '安全帽',
              type: 'bar',
              data: this.dataMoon.dataM2,
              markPoint: {
                data: [{
                    type: 'max',
                    name: '最大值'
                  },
                  {
                    type: 'min',
                    name: '最小值'
                  }
                ]
              },
              markLine: {
                data: [{
                  type: 'average',
                  name: '平均值'
                }]
              }
            },
            // {
            //   name: '工作服',
            //   type: 'bar',
            //   data: this.dataMoon.dataM3,
            //   markPoint: {
            //     data: [{
            //         type: 'max',
            //         name: '最大值'
            //       },
            //       {
            //         type: 'min',
            //         name: '最小值'
            //       }
            //     ]
            //   },
            //   markLine: {
            //     data: [{
            //       type: 'average',
            //       name: '平均值'
            //     }]
            //   }
            // }
          ]
        })
      }
    }
  }
</script>

<style scoped>
  #myChart {
    background: #dddddd;
  }

  .echarts {
    background: #dddddd;
    width: 100%;
    height: 100%;
  }
</style>