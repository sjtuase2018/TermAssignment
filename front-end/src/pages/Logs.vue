<template>
  <div>
    <v-container>
      <v-toolbar flat color="grey">
        <v-toolbar-title>LOGS</v-toolbar-title>
        <v-divider class="mx-2" inset vertical></v-divider>
        <v-spacer></v-spacer>
        <v-text-field v-model="search" append-icon="search" label="Search" single-line hide-details></v-text-field>
      </v-toolbar>
      <v-data-table dark :headers="headers" :items="desserts" :search="search" prev-icon="skip_previous" next-icon="skip_next"
        sort-icon="mdi-menu-down" class="elevation-1">
        <template slot="items" slot-scope="props">
          <td class="text-xs-center">{{ props.item.area }}</td>
          <td class="text-xs-center">{{ props.item.hazardCategory }}</td>
          <td class="text-xs-center">{{ props.item.time }}</td>
          <td class="text-xs-center">
            <v-dialog v-model="dialog" width="500">
              <v-btn slot="activator" color="red lighten-2" dark>
                Click Me
              </v-btn>
              <v-card>
                <v-card-title class="headline grey" primary-title>
                  PictureShot
                </v-card-title>
                <v-img :src= "props.item.imgUrl"/>
                <v-card-text>
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore
                  et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
                  aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
                  cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa
                  qui officia deserunt mollit anim id est laborum.
                </v-card-text>
                <v-divider></v-divider>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="primary" flat @click="dialog = false">
                    Close
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </td>
        </template>
        <template slot="no-data">
          <v-btn color="primary" @click="initialize">Reset</v-btn>
        </template>
        <v-alert slot="no-results" :value="true" color="error" icon="warning">
          Your search for "{{ search }}" found no results.
        </v-alert>
      </v-data-table>
    </v-container>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    data: () => ({
      dialog: false,
      search: '',
      pagesize: 10,
      sortby: 'time',
      startwith: 0,
      headers: [{
          text: 'Area',
          sortable: false,
          align: 'center',
          value: 'area'
        },
        {
          text: 'HazardCategory',
          sortable: false,
          align: 'center',
          value: 'hazardCategory'
        },
        {
          text: 'Time',
          sortable: false,
          align: 'center',
          value: 'time'
        },
        {
          text: 'PictureShot',
          sortable: false,
          align: 'center',
          value: 'pictureShot'
        },
      ],
      desserts: [],
      editedIndex: -1,
      editedItem: {
        date: '',
        area: 0,
        hazardCategory: 0,
        time: ''
      },
      defaultItem: {
        date: '',
        area: 0,
        hazardCategory: 'A',
        time: ''
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

    created() {
        const path = `http://localhost:5000/api/getLogs/`;
        axios.post(path,{
          pagesize: 10,
          sortby: 'time',
          startwith: 0,
        }).then(response => {
            console.log(response.data),
            this.desserts = response.data
          })
          .catch(error => {
            console.log(error)
          })
    },

    methods: {
      showPicture() {
        this.dialog = true
      }
    }
  }
</script>

<style scoped>
</style>