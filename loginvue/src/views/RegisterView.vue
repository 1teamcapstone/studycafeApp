<template>
    <div class="register">
      <p>회원가입</p>
      <input type="text" placeholder="ID"><br>
      <input type="password" placeholder="PASSWORD"><br>
      <input type="text" placeholder="NAME"><br>
      <input type="text" placeholder="NICKNAME"><br>
      <input type="number" placeholder="PHONENUMBER"><br>
      <b-button variant="primary">회원가입하기</b-button>
      <span>또는 <router-link to="/login">로그인</router-link>으로 돌아가기</span>
    </div>
</template>
  
<script>
    export default {
      name: 'signUp',
      data() {
        return {
        }
      },
      methods: { }
    }
</script>
  
<style scoped>
    .signUp {
      margin-top: 40px;
    }
    input {
      margin: 10px 0;
      width: 20%;
      padding: 15px;
    }
    button {
      margin-top: 20px;
      width: 10%;
      cursor: pointer;
    }
    p {
      margin-top: 40px;
      font-size: 20px;
    }
    span {
      display: block;
      margin-top: 20px;
      font-size: 15px;
    }
</style>