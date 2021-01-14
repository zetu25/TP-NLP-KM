<template>
  <div
    class="container mx-auto text-base sm:text-base md:text-lg lg:text-xl xl:text-xl"
  >
    <img
      class="mx-auto w-56 h-40 object-cover object-top"
      src="@/assets/images/unicaen.png"
    />
    <form class="relative h-16">
      <input
        class="w-full h-full px-8 rounded mb-8 focus:outline-none focus:shadow-outline shadow-lg"
        type="search"
        placeholder="What do you search for?"
        v-model="search"
      />
      <input
        type="number"
        class="text-center"
        placeholder="Insert n° of similar words"
        v-model="this.$store.state.get_synonym_number"
        @change="this.$store.commit('set_synonym_number', this)"
      />
      <button
        type="button"
        @click.prevent="get_results()"
        class="inline-flex items-center absolute top-0 right-0 bottom-0 mt-1 mr-1 mb-1 px-4 py-2 border border-transparent text-base leading-6 font-medium font-sans rounded-md text-white bg-black hover:bg-gray-900 focus:outline-none focus:shadow-outline-indigo transition"
      >
        <svg
          class="animate-spin -ml-1 mr-3 h-5 w-5 text-white"
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
  </div>
</template>


<script>
import axios from "axios";
import router from "@/router/router";

export default {
  name: "Home",
  data() {
    return {
      search: "",
      show: false,
      router,
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
          this.$store.commit("set_synonym_number", this);
          this.$store.commit("set_synonyms", synonyms);
          router.push("/results");
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


