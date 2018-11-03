<template>
  <div>
    <v-container>
      <v-toolbar flat color="grey">
        <v-toolbar-title>SEETTING</v-toolbar-title>
        <v-divider class="mx-2" inset vertical></v-divider>
        <v-spacer></v-spacer>
        <v-dialog v-model="dialog" max-width="500px">
          <v-btn slot="activator" color="primary" dark class="mb-2" @click="setNew">New Item</v-btn>
          <v-card>
            <v-card-title>
              <span class="headline">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container grid-list-md>
                <v-layout wrap>
                  <v-flex xs12 sm6 md4>
                    <v-text-field v-model="editedItem.area" label="Area （地区）"></v-text-field>
                  </v-flex>
                  <v-flex xs12 sm6 md4>
                    <v-text-field v-model="editedItem.rules" label="Rules （危险类别）"></v-text-field>
                  </v-flex>
                </v-layout>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" flat @click.native="close">Cancel</v-btn>
              <v-btn color="blue darken-1" flat @click.native="save(editedItem)">Save</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
      <v-data-table :headers="headers" :items="desserts" v-model="desserts" hide-actions class="elevation-1">
        <template slot="items" slot-scope="props">
          <td class="text-xs-center">{{ props.item.area }}</td>
          <td class="text-xs-center">
            <div v-for="(item,index) in props.item.rules" :key="index">{{item}}</div>
          </td>
          <td class="justify-center layout px-0">
            <v-icon small class="mr-2" @click="editItem(props.item)">
              edit
            </v-icon>
            <v-icon small @click="deleteItem(props.item)">
              delete
            </v-icon>
          </td>
        </template>
      </v-data-table>
    </v-container>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    data: () => ({
      dialog: false,
      new: false,
      headers: [
        {
          text: 'Area (地区）',
          align: 'center',
          sortable: false,
          value: 'area'
        },
        {
          text: 'Rules (危险类别）',
          align: 'center',
          sortable: false,
          value: 'rules'
        },
        {
          text: 'Actions',
          value: 'name',
          align: 'center',
          sortable: false
        }
      ],
      desserts: [],
      editedIndex: -1,
      editedItem: {
        id: '',
        area: 0,
        rules: ['无人区','安全帽','工作服'],
      },
      defaultItem: {
        id: '',
        area: 0,
        rules: ['无人区','安全帽','工作服'],
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
      }
    },
    mounted() {
      this.getCamera();
    },
    created() {

    },

    methods: {
      getCamera() {
        const path = `http://localhost:5000/api/getCamera/`;
        axios.get(path, {

          }).then(response => {
            console.log(response.data)
            this.desserts = response.data
            console.log(this.desserts)
          })
          .catch(error => {
            console.log(error)
          })
      },
      editItem(item) {
        this.editedIndex = this.desserts.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true

        // //发送修改请求
        // const path = `http://localhost:5000/api/settingEdit/`;
        // axios.post(path, {
        //   item
        // }).then(response => {
        //     console.log(response.data),
        //     this.desserts = response.data
        //   })
        //   .catch(error => {
        //     console.log(error)
        //   })
      },

      deleteItem(item) {
        const index = this.desserts.indexOf(item)
        var id = item.id
        var r = confirm('Are you sure you want to delete this item?') && this.desserts.splice(index, 1)
        if (r) {
          //发送删除请求
          const path = `http://localhost:5000/api/settingDelete/`;
          axios.post(path, {
              id
            }).then(response => {
              console.log(response.data),
                this.desserts = response.data
                this.$set(this.desserts)
                // this.$router.push('/setting') 
            })
            .catch(error => {
              console.log(error)
            })
        }
      },

      close() {
        this.dialog = false
        // setTimeout(() => {
        //   this.editedItem = Object.assign({}, this.defaultItem)
        //   this.editedIndex = -1
        // }, 300)
      },

      save(item) {
        // if (this.editedIndex > -1) {
        //   Object.assign(this.desserts[this.editedIndex], this.editedItem)
        // } else {
        //   this.desserts.push(this.editedItem)

        // }
        //发送修改请求
        if (this.new) {
          const path = `http://localhost:5000/api/settingNew/`;
          axios.post(path, {
              id: item.id,
              area: item.area,
              rules: item.rules
            }).then(response => {
              console.log(response.data),
                this.desserts = response.data
                this.$set(this.desserts)
            })
            .catch(error => {
              console.log(error)
            })
          this.close()
          this.new = false
        } else {
          const path = `http://localhost:5000/api/settingSave/`;
          axios.post(path, {
              id: item.id,
              area: item.area,
              rules: item.rules
            }).then(response => {
              console.log(response.data),
                this.desserts = response.data
                this.$set(this.desserts)

            })
            .catch(error => {
              console.log(error)
            })
          this.close()
        }
      },

      setNew () {
        this.new = true
      }
    }
  }
</script>

<style scoped>
</style>