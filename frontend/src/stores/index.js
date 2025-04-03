import { defineStore } from "pinia";
import { ref, computed } from 'vue';

export const useUserStore = defineStore('user', () => {
    // ============= State =============
    const token = ref('')
    const user_id = ref('')
    
    // 初始化状态
    const initState = () => {
        try {
            token.value = uni.getStorageSync('token') || ''
            user_id.value =  uni.getStorageSync('user_id') || ''
        } catch (error) {
            clearUser()
        }
    }
    
    // 初始化
    initState()

    // ============= Getters =============
    const isLoggedIn = computed(() => !!token.value)

    // ============= Actions =============
    function setUser(userData, userToken) {
        if (!userData || !userToken) return false
        try {
            user_id.value = userData
            token.value = userToken
            uni.setStorageSync('user_id', userData)
            uni.setStorageSync('token', userToken)
            return true
        } catch (error) {
            console.error('存储用户信息失败:', error)
            return false
        }
    }

    function clearUser() {
        user_id.value = null
        token.value = ''
        try {
            uni.removeStorageSync('user_id')
            uni.removeStorageSync('token')
        } catch (error) {
            console.error('清除用户信息失败:', error)
        }
    }

    return {
        // State
        token,
        user_id,
        
        // Getters
        isLoggedIn,
        
        // Actions
        setUser,
        clearUser,
        initState
    }
}, {
    persist: false // 禁用 Pinia 持久化，使用自定义存储
})