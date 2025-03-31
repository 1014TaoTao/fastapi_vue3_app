<template>
	<view class="layout">
		<view class="header">
			<view class="user-profile">
				<image class="avatar" :src="'/static/logo.png'"></image>
				<view class="user-info">
					<text class="name">{{ userInfo.name || '未登录' }}</text>
					<text class="meta">
						@{{ userInfo.username || '未登录' }}
					</text>
				</view>
			</view>
			<view class="actions">
				<button v-if="userInfo.is_superuser" type="default" class="action-btn" @click="handleGoUsers">用户列表</button>
				<button type="warn" class="action-btn" @click="handleLogout">退出登录</button>
			</view>
		</view>

		<view class="main">
			<slot name="main"></slot>
		</view>

	</view>
</template>

<script setup>
import { ref } from "vue";
import { onLoad } from "@dcloudio/uni-app";
import { detail_user, logout } from "../../api/apis";
const userInfo = ref({
	name: "",
	username: "",
	avatar: "",
	is_superuser: false,
});

const tokenData = ref({
	token: uni.getStorageSync('token'),
});

const user_id = uni.getStorageSync('user_id');

onLoad(() => {
	console.log('tokenData', tokenData.value);
	console.log('user_id', user_id);
	handleDetail();
});

// 获取当前登录用户信息
async function handleDetail() {
	detail_user(user_id).then(res => {
		console.log('用户详情', res);
		userInfo.value = res.data;
		uni.showToast({ title: res.message, icon: 'success' });
	});
}

// 退出登录
async function handleLogout() {
	logout(tokenData.value).then(res => {
		console.log('退出登录', res);
		uni.removeStorageSync('token');
		uni.removeStorageSync('user_id');
		uni.reLaunch({ url: '/pages/login/login' });
	});
}

// 跳转用户列表
async function handleGoUsers() {
	uni.navigateTo({ url: '/pages/me/users' });
}


</script>

<style lang="scss">
.layout {
	position: fixed;
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
	display: flex;
	flex-direction: column;
	height: 100vh;
	width: 100vw;
	overflow: hidden;

	.header {
		position: absolute;
		top: 44px;
		left: 20rpx;
		right: 20rpx;
		min-height: 100rpx;
		background: linear-gradient(135deg, #c63a35 0%, #fab4b0 100%);
		z-index: 100;
		padding: 30rpx;
		border-radius: 30rpx;
		box-shadow: 0 4rpx 20rpx rgba(79, 172, 254, 0.3);
		margin-bottom: 20rpx;
		display: flex;
		justify-content: space-between;
		align-items: center;
		backdrop-filter: blur(10px);

		.user-profile {
			display: flex;
			align-items: center;
			gap: 20rpx;
			
			.avatar {
				width: 100rpx;
				height: 100rpx;
				border-radius: 50%;
				border: 4rpx solid rgba(255, 255, 255, 0.8);
				box-shadow: 0 4rpx 10rpx rgba(0, 0, 0, 0.1);
			}
			
			.user-info {
				display: flex;
				flex-direction: column;
				
				.name {
					font-size: 36rpx;
					font-weight: bold;
					color: #ffffff;
					margin-bottom: 4rpx;
					text-shadow: 0 2rpx 4rpx rgba(0, 0, 0, 0.1);
				}
				
				.meta {
					font-size: 24rpx;
					color: rgba(255, 255, 255, 0.8);
				}
			}
		}
		
		.actions {
			display: flex;
			gap: 20rpx;
			
			.action-btn {
				padding: 0 30rpx;
				height: 60rpx;
				line-height: 60rpx;
				border-radius: 30rpx;
				font-size: 26rpx;
				border: none;
				
				&[type="warn"] {
					background: rgba(255, 255, 255, 0.2);
					color: #fff;
				}
			}
		}
	}


	.main {
		position: absolute;
		top: 240rpx;
		left: 0;
		right: 0;
		bottom: 66.49px;
		overflow-y: auto;
		background: #f8f8f8;
		padding: 20rpx;
		padding-bottom: 80rpx;
	}

}
</style>