<template>
  <div
    class="w-full flex items-center justify-center bg-teal-lightest font-sans"
  >
    <!--  lg:max-w-lg -->
    <div class="bg-white rounded shadow p-6 m-4 w-full lg:w-3/4">
      <h1 class="text-grey-darkest text-4xl mb-8">Search Results</h1>
      <div class="mb-4 flex">
        <form class="relative h-10 w-2/3 flex-auto">
          <input
            class="w-full h-full px-4 rounded mb-8 focus:outline-none focus:shadow-outline shadow-lg"
            type="search"
            placeholder="What do you search for?"
            v-model="search"
          />
          <button
            type="submit"
            @click.prevent="get_results()"
            class="inline-flex items-center absolute top-0 right-0 bottom-0 mt-1 mr-1 mb-1 px-4 py-2 border border-transparent text-base leading-6 font-medium font-sans rounded-md text-white bg-black hover:bg-gray-900 focus:outline-none focus:shadow-outline-indigo transition"
          >
            <svg
              class="animate-spin -ml-6 mr-1 h-5 w-12 text-white"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              v-if="show"
            >
              <circle
                class="opacity-25"
                cx="12"
                cy="12"
                r="10"
                stroke="currentColor"
                stroke-width="4"
              ></circle>
              <path
                class="opacity-75"
                fill="currentColor"
                d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
              ></path>
            </svg>
            Search
          </button>
        </form>
        <input
          type="number"
          class="text-center"
          placeholder="Insert n° of similar words"
          v-model="this.$store.state.get_synonym_number"
          @change="this.$store.commit('set_synonym_number', this)"
        />
      </div>

      <div class="grid grid-cols-12 gap-4">
        <div class="col-span-2">
          <h2>Mots sémantiquement proches :</h2>
          <hr />
          <ul class="list-decimal">
            <li v-for="syno in synonyms" :key="syno">
              {{ syno }}
            </li>
          </ul>
        </div>
        <div class="col-span-10 mb-4 text-left">
          <ul>
            <li v-for="link in results" :key="link">
              <a target="_blank" v-bind:href="link">{{ link }}</a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Collection",

  data() {
    return {
      search: "",
      synonym: "",
      show: false,
    };
  },
  methods: {
    get_results() {
      this.show = !this.show;
      axios
        .post("http://localhost:5000/get_search_results", {
          entities: [this.search, this.synonym_number],
        })
        .then((response) => {
          let synonyms = [];
          let results = [];
          Object.entries(response.data).forEach(([key, value]) => {
            synonyms.push(key);
            value.forEach((element) => {
              results.push(element);
            });
          });
          let uniqueSet = new Set(results);
          results = [...uniqueSet];
          this.$store.commit("set_results", results);
          this.$store.commit("set_synonyms", synonyms);
          this.$router.push("/results");
          this.show = !this.show;
        })
        .catch((e) => {
          this.errors.push(e);
        });
    },
  },
  computed: {
    results() {
      return this.$store.getters.get_result;
    },
    synonyms() {
      return this.$store.getters.get_synonyms;
    },
    synonym_number() {
      return this.$store.state.get_synonym_number;
    },
  },
};
</script>

<style>
</style>