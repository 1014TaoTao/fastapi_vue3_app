import { defineStore } from "pinia";
import { ref, computed, reactive, toRefs } from 'vue';

export const useUserStore = defineStore('user', () => {
    // ============= State =============
    const state = reactive({
        token: uni.getStorageSync('token') || '',
        userInfo: uni.getStorageSync('userInfo') || null
    })

    // ============= Getters =============
    const getters = {
        getToken: computed(() => !!state.token),
        getUserInfo: computed(() => state.userInfo)
    }

    // ============= Actions =============
    const actions = {
        // 设置用户信息
        setUser(userData) {
            if (!userData) return false
            try {
                state.userInfo = userData
                uni.setStorageSync('userInfo', userData)
                return true
            } catch (error) {
                console.error('存储用户信息失败:', error)
                return false
            }
        },

        // 设置token
        setToken(token) {
            if (!token) return false
            try {
                state.token = token
                uni.setStorageSync('token', token)
                return true
            } catch (error) {
                console.error('存储token失败:', error)
                return false
            }
        },

        // 设置store
        setStore(userData, userToken) {
            return this.setUser(userData) && this.setToken(userToken)
        },

        // 清理状态
        clear() {
            state.userInfo = null
            state.token = ''
            try {
                uni.removeStorageSync('userInfo')
                uni.removeStorageSync('token')
            } catch (error) {
                console.error('清除用户信息失败:', error)
            }
        }
    }

    return {
        ...toRefs(state),
        ...getters,
        ...actions
    }
})