import { createStore } from "vuex";

const store = createStore({
    state: {
        result: [],
        search_term: "",
        synonym_number: 5,
        synonyms:[],
        loader: false
    },
    mutations: {
        set_results(state,result){
            state.result = result;
        },
        set_loader(state,loader){
            state.loader = loader;
        },
        set_synonym_number(state,synonym){
            state.synonym_number = synonym
        },
        set_synonyms(state,synonyms){
            state.synonyms = synonyms
        }
    },
    getters: {
        get_loader: state => state.loader,
        get_synonym_number: state => state.synonym_number,
        get_synonyms: state => state.synonyms,
        get_result: state => state.result
    }
});

export default store;