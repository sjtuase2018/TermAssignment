<template>
  <div>
    <v-container>
      <v-toolbar flat color="grey">
        <v-toolbar-title>SEETTING</v-toolbar-title>
        <v-divider class="mx-2" inset vertical></v-divider>
        <v-spacer></v-spacer>
        <v-dialog v-model="dialog" max-width="500px">
          <v-btn slot="activator" color="primary" dark class="mb-2">New Item</v-btn>
          <v-card>
            <v-card-title>
              <span class="headline">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container grid-list-md>
                <v-layout wrap>
                  <v-flex xs12 sm6 md4>
                    <v-text-field v-model="editedItem.id" label="Id (序号）"></v-text-field>
                  </v-flex>
                  <v-flex xs12 sm6 md4>
                    <v-text-field v-model="editedItem.area" label="Area （地区）"></v-text-field>
                  </v-flex>
                  <v-flex xs12 sm6 md4>
                    <v-text-field v-model="editedItem.dangerLevel" label="DangerLevel （危险类别）"></v-text-field>
                  </v-flex>
                </v-layout>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" flat @click.native="close">Cancel</v-btn>
              <v-btn color="blue darken-1" flat @click.native="save">Save</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
      <v-data-table :headers="headers" :items="desserts" hide-actions class="elevation-1">
        <template slot="items" slot-scope="props">
          <td class="text-xs-center">{{ props.item.id }}</td>
          <td class="text-xs-center">{{ props.item.area }}</td>
          <td class="text-xs-center">{{ props.item.hazardCategory }}

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
        <template slot="no-data">
          <v-btn color="primary" @click="initialize">Reset</v-btn>
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
      headers: [{
          text: 'ID (序号）',
          align: 'center',
          sortable: false,
          value: 'id'
        },
        {
          text: 'Area (地区）',
          align: 'center',
          sortable: false,
          value: 'area'
        },
        {
          text: 'HazardCategory (危险类别）',
          align: 'center',
          sortable: false,
          value: 'hazardCategory'
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
        hazardCategory: 0,
      },
      defaultItem: {
        id: '',
        area: 0,
        hazardCategory: 0,
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
        const path = `http://localhost:5000/api/getCamera/`;
        axios.get(path,{

        }).then(response => {
            console.log(response.data)
            this.desserts = response.data
          })
          .catch(error => {
            console.log(error)
          })
    },
    created() {

    },

    methods: {
      editItem(item) {
        this.editedIndex = this.desserts.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true

        //发送修改请求
        const path = `http://localhost:5000/api/settingEdit/`;
        axios.post(path, {
          item
        }).then(response => {
            console.log(response.data),
            this.desserts = response.data
          })
          .catch(error => {
            console.log(error)
          })
      },

      deleteItem(item) {
        const id = this.desserts.indexOf(item)
        var r = confirm('Are you sure you want to delete this item?') && this.desserts.splice(id, 1)
        if (r) {
          //发送删除请求
        const path = `http://localhost:5000/api/settingDelete/`;
        axios.delete(path, {
          id
        }).then(response => {
            console.log(response.data),
            this.desserts = response.data
          })
          .catch(error => {
            console.log(error)
          })
        }
      },

      close() {
        this.dialog = false
        setTimeout(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        }, 300)
      },

      save() {
        if (this.editedIndex > -1) {
          Object.assign(this.desserts[this.editedIndex], this.editedItem)
        } else {
          this.desserts.push(this.editedItem)
        }
        this.close()
      }
    }
  }
</script>

<style scoped>
</style>