<template>
  <div>
    <v-container>
      <v-toolbar flat color="grey">
        <v-toolbar-title>日志</v-toolbar-title>
        <v-divider class="mx-2" inset vertical></v-divider>
        <v-spacer></v-spacer>
          <v-dialog v-model="dia" width="500" dark>
              <!-- <v-btn slot="activator" color="primary" dark> -->
              <v-card> 
                <v-card-text>
                  <img class='img' :src="pic_path_temp" />
                </v-card-text>
              </v-card>
            </v-dialog>
        <v-text-field v-model="search" append-icon="search" label="搜索" single-line hide-details @keyup.enter="getLogs"></v-text-field>
      </v-toolbar>
      <v-data-table dark :headers="headers" :items="desserts" :pagination.sync="pagination" :total-items="totalDesserts" no-data-text="没有数据"
        :rows-per-page-items="rowsPerPageItems" :loading="loading" prev-icon="skip_previous" next-icon="skip_next" sort-icon="mdi-menu-down" class="elevation-1">
        <template slot="items" slot-scope="props">
          <td class="text-xs-center">{{ props.item.area }}</td>
          <td class="text-xs-center">{{ props.item.rule }}</td>
          <td class="text-xs-center">{{ props.item.date }}</td>
          <td class="text-xs-center">
            <img id='img' :style="{width:'50px', height:'50px'}" :src="props.item.pic_path" @click="showImage(props.item.pic_path)" />
            
          </td>
        </template>
        <v-alert slot="no-results" :value="true" color="error" icon="warning">
          对不起，找不到"{{ search }}"
        </v-alert>
      </v-data-table>
    </v-container>
  </div>
</template>

<script>
  import axios from 'axios'
  
  // import '../assets/images/pic0.jpg'
  export default {
    data: () => ({
      pic_path_temp: '',
      dia: false,
      search: '',
      pagesize: 10,
      sortby: 'date',
      startwith: 0,
      totalDesserts: 0,
      loading: true,
      pagination: {},
      rowsPerPageItems: [5, 10, 25, 100],
      headers: [{
          text: '地区',
          sortable: false,
          align: 'center',
          value: 'area'
        },
        {
          text: '规则',
          sortable: false,
          align: 'center',
          value: 'rule'
        },
        {
          text: '日期',
          sortable: true,
          align: 'center',
          value: 'date'
        },
        {
          text: '图片',
          sortable: false,
          align: 'center',
          value: 'pic_path'
        },
      ],
      desserts: [],
      editedIndex: -1,
      editedItem: {
        date: '',
        area: 0,
        rule: 0,
        pic_path: ''
      },
      defaultItem: {
        date: '',
        area: 0,
        rule: 'A',
        pic_path: ''
      }
    }),

    computed: {
      formTitle() {
        return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
      }
    },

    watch: {
      dialog(val) {
        val || this.close()
      },
      pagination: {
        handler() {
          this.getDataFromApi()
          // .then(data => {
          //     this.desserts = data.items
          //     this.totalDesserts = data.total
          //   })
        },
        deep: true
      }
    },

    mounted() {
      this.getDataFromApi()
      // .then(data => {
      //     this.desserts = data.items
      //     this.totalDesserts = data.total
      //   })
    },

    created() {
      //this.getLogs();
    },

    methods: {
      showImage(pic_path) {
        this.dia = true;
        this.pic_path_temp = pic_path;
      },
      getLogs() {
        let moment = require("moment");
        if (this.search) {
          const path = `http://localhost:5000/api/getLogs/`;
          axios.post(path, {
              pagesize: this.pagination.rowsPerPage,
              sortby: this.pagination.sortBy,
              startwith: (this.pagination.page - 1) * this.pagination.rowsPerPage,
              search: this.search
            }).then(response => {
              //console.log(response.data),
              this.desserts = response.data.logs
              this.totalDesserts = response.data.length
              this.desserts.forEach(element => {
                element.date = moment(element.date).utcOffset(0).format('YYYY-MM-DD HH:mm:ss')
              });
            })
            .catch(error => {
              console.log(error)
            })
            .finally(() => this.loading = false);
        } else {
          const path = `http://localhost:5000/api/getLogs/`;
          axios.post(path, {
              pagesize: this.pagination.rowsPerPage,
              sortby: this.pagination.sortBy,
              startwith: (this.pagination.page - 1) * this.pagination.rowsPerPage,
            }).then(response => {
              //console.log(response.data),
              this.desserts = response.data.logs
              this.totalDesserts = response.data.length
              this.desserts.forEach(element => {
                element.date = moment(element.date).utcOffset(0).format('YYYY-MM-DD HH:mm:ss')
              });
            })
            .catch(error => {
              console.log(error)
            })
            .finally(() => this.loading = false);
        }
      },

      getDataFromApi() {
        this.loading = true

        this.getLogs()

      },

      close() {
        this.dialog = false;
      }
    }
  }
</script>

<style scoped>
.img {
  width: 460px;
  height: 400px;
}
</style>