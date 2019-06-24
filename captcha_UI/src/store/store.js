import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import { stat } from 'fs';


Vue.use(Vuex)

const api_url = 'http://localhost:5000/detection'

export const store = new Vuex.Store({
    state: {
        result: null,
        capcha: null,
    },
    getters: {
        result(state) {
            return state.result
        },
        capcha(state){
            return state.capcha
        },
    },
    mutations: {
        set_result(state, rep) {
            state.result = "data:image/jpeg;base64,"+rep;
        },
        clear_result(state) {
            state.result = null;
            state.capcha = null;
        },
    },
    actions: {
        test(context, dt) {
            return new Promise((resolve, reject)=>{
                axios.post(api_url,dt).then(response => {
                var imgData = response.data['base64'];
                var imgHeader = response.data['header'];
                var capcha = response.data['capcha']       
                if (imgData){
                    context.state.result = imgHeader+","+ imgData;
                    context.state.capcha = capcha;
                    console.log(response);
                }
                resolve(response);
            }).catch(error=>{
                reject(error)
            })
        })
        },
        clear_result(context)
        {
            context.commit('clear_result');
        }
}})