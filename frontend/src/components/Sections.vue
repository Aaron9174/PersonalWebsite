<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1> Sections </h1>
        <hr><br><br>
        <b-button type="button"
                  class="btn btn-success btn-sm"
                  v-b-modal.section-modal>
                    Add Section
        </b-button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Purpose</th>
              <th scope="col">Author</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(section, index) in sections" :key="index">
              <td>{{section.title}}</td>
              <td>{{section.purpose}}</td>
              <td>{{section.author}}</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">Update</button>
                  <button type="button" class="btn btn-danger btn-sm">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addSectionModal"
              id="section-modal"
              title="Add a new section"
              hide-footer>
        <b-form @submit="onSubmit" @reset="onReset" class="w-100">
          <b-form-group id="form-title-group"
                        label="Title:"
                        label-for="form-title-input">
              <b-form-input id="form-title-input"
                            type="text"
                            v-model="addSectionForm.title"
                            required
                            placeholder="Enter title">
              </b-form-input>
          </b-form-group>
          <b-form-group id="form-author-group"
                        label="Author:"
                        label-for="form-author-input">
              <b-form-input id="form-author-input"
                            type="text"
                            v-model="addSectionForm.author"
                            required
                            placeholder="Enter author">
              </b-form-input>
          </b-form-group>
          <b-form-group id="form-purpose-group"
                        label="Purpose:"
                        label-for="form-purpose-input">
              <b-form-input id="form-purpose-input"
                            type="text"
                            v-model="addSectionForm.purpose"
                            required
                            placeholder="Enter purpose">
              </b-form-input>
          </b-form-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      sections: [],
      addSectionForm: {
        title: '',
        author: '',
        purpose: '',
      },
    };
  },
  methods: {
    getSections() {
      const path = 'http://localhost:5000/sections';
      axios.get(path)
        .then((res) => {
          this.sections = res.data.sections;
          // eslint-disable-next-line
          console.log(this.sections);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addSection(payload) {
      const path = 'http://localhost:5000/sections';
      axios.post(path, payload)
        .then(() => {
          this.getSections();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getSections();
        });
    },
    initForm() {
      this.addSectionForm.title = '';
      this.addSectionForm.author = '';
      this.addSectionForm.purpose = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addSectionModal.hide();
      const payload = {
        title: this.addSectionForm.title,
        author: this.addSectionForm.author,
        purpose: this.addSectionForm.purpose,
      };
      this.addSection(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addSectionModal.hide();
      this.initForm();
    },
  },
  created() {
    this.getSections();
  },
};
</script>

<style>
  @import '../assets/css/sections.css';
</style>>
