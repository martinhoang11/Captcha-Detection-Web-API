<template>
    <div>
        <div class="content">
            <div v-if="!imgSrc">
                <br>Chọn ảnh chứa captcha cần demo:
                <input type="file" @change="chooseImg">
            </div>
            <div v-if="imgSrc">
                <h3>Ảnh demo:</h3>
                <button @click="removeImage">Delete</button>
                <button @click="start">Start</button>
            </div>
        </div>

        <div class="content">
            <img class="imgSrc" :src="imgSrc">
        </div>

        <div class="content-result" v-if="started == true && imgSrc">
            <h3 class="left">Ảnh kết quả:</h3>
            <h3 class="right">Captcha giải được: <span>{{capcha}}</span></h3>
            

            <div class="left">
                <img class="result" v-if="result" :src="result">
                <img class="result" v-else src="../img/loading.gif">
            </div>
            
        </div>
    </div>
</template>

<script>
export default {
    name: "appBody",
    data() {
        return {
            imgSrc: "",
            started: false
        };
    },
    computed: {
        result() {
            return this.$store.getters.result;
        },
        capcha(){
            return this.$store.getters.capcha;
        }
    },
    methods: {
        chooseImg(e) {
            var files = e.target.files || e.dataTransfer.files;
            if (!files.length) {
                return;
            }
            this.createImage(files[0]);
        },
        createImage(file) {
            var reader = new FileReader();
            reader.onload = e => {
            this.imgSrc = e.target.result;
           
        };
        reader.readAsDataURL(file);
        },
        removeImage() {
            this.started = false;
            this.imgSrc = "";
            this.$store.dispatch("clear_result");
        },
        start() {
            this.started = true;
            var data = new FormData();
            data.append("imgSrc", this.imgSrc);
            this.$store.dispatch("test", data);
        }
    }
};
</script>

<style scoped>
.content {
    padding-left: 50px;
    font-size: 125%;
}
.content-result {
    padding-left: 20%;
    font-size: 125%;
}
.result {
    max-height: 600px;
    width: auto;
    margin-bottom: 75px;

}
.right{
    float: right;
    padding-right: 35%;
    text-align: left;
}
.left{
    float: left;
}
.imgSrc {
    max-height: 200px;
}
span{
    color: red;
}
</style>
