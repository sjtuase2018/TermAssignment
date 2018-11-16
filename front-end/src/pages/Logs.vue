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
          <td class="text-xs-center">{{ props.item.rule }}</td>
          <td class="text-xs-center">{{ props.item.date }}</td>
          <td class="text-xs-center">
            <v-dialog v-model="dialog" width="500">
              <v-btn slot="activator" color="red lighten-2" dark>
                Click Me
              </v-btn>
              <v-card>
                <v-card-title class="headline grey" primary-title>
                  PictureShot
                </v-card-title>
                <v-card-text>
                  <v-img :src="props.item.pic_path" />
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
      sortby: 'date',
      startwith: 0,
      headers: [{
          text: 'Area',
          sortable: false,
          align: 'center',
          value: 'area'
        },
        {
          text: 'Rule',
          sortable: false,
          align: 'center',
          value: 'rule'
        },
        {
          text: 'Date',
          sortable: true,
          align: 'center',
          value: 'date'
        },
        {
          text: 'PictureShot',
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
      }
    },

    created() {
      this.getLogs();
    },

    methods: {
      showPicture() {
        this.dialog = true
      },
      getLogs() {
        const path = `http://localhost:5000/api/getLogs/`;
        axios.post(path, {
            pagesize: this.pagesize,
            sortby: this.sortby,
            startwith: this.startwith,
          }).then(response => {
            console.log(response.data),
            this.desserts = response.data
          })
          .catch(error => {
            console.log(error)
          })
      },

    }
  }
</script>

<style scoped>
</style>