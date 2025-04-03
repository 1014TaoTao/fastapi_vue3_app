<template>
	<view>
		<app-layout>
			<template #main>
				<view class="user-list-container">
					<!-- 搜索区域 -->
					<view class="search-area">
						<uni-search-bar class="search-input" placeholder="请输入用户名" @confirm="handleSearch"
							v-model="searchQuery" @clear="handleSearch">
						</uni-search-bar>
					</view>

					<!-- 用户列表区域 -->
					<uni-section title="用户列表" type="line" padding>
						<uni-list :border="true">
							<uni-list-item v-for="item in tableData"
								:avatar="item.avatar || '/static/default-avatar.png'" :key="item.id" :title="item.name"
								:note="item.created_at" :show-badge="true" :badge-text="item.disabled ? '禁用' : '启用'"
								:badge-style="item.disabled ? disabledBadgeStyle : enabledBadgeStyle" clickable
								@click="showDetailPopup(item)">
								<!-- 左侧头像 -->
								<template v-slot:header>
									<view class="avatar-wrapper">
										<image class="avatar" :src="item.avatar || '/static/default-avatar.png'"
											mode="widthFix"></image>
									</view>
								</template>
							</uni-list-item>
						</uni-list>
					</uni-section>

					<!-- 加载更多 -->
					<uni-load-more :status="loadStatus" :content-text="{
						contentdown: '上拉加载更多',
						contentrefresh: '正在加载...',
						contentnomore: '没有更多数据了'
					}" @clickLoadMore="loadMore" />
				</view>

				<!-- 详情弹窗 -->
				<uni-popup ref="detailPopup" type="center" :is-mask-click="true">
					<view class="popup-content">
						<view class="popup-header">
							<text class="popup-title">{{ popupTitle }}</text>
							<uni-icons type="closeempty" size="24" color="#999" @click="closeDetailPopup"></uni-icons>
						</view>
						<scroll-view class="popup-body" scroll-y>
							<view class="detail-item" v-for="(value, key) in currentDetail" :key="key">
								<text class="detail-label">{{ formatLabel(key) }}:</text>
								<text class="detail-value">{{ formatValue(key, value) }}</text>
							</view>
						</scroll-view>
						<view class="popup-footer">
							<button class="popup-button" @click="closeDetailPopup">关闭</button>
						</view>
					</view>
				</uni-popup>
			</template>
		</app-layout>
	</view>
</template>

<script setup>
import { ref, reactive } from "vue";
import { onLoad } from "@dcloudio/uni-app";
import {
	list_user,
	detail_user,
} from "@/api/apis";

// 状态定义
const loadStatus = ref('more');
const searchQuery = ref('');
const tableData = ref([]);
const detailPopup = ref(null);
const currentDetail = ref({});
const popupTitle = ref('');

// 徽章样式
const enabledBadgeStyle = reactive({
	backgroundColor: '#0f0',
	color: '#fff'
});
const disabledBadgeStyle = reactive({
	backgroundColor: '#f00',
	color: '#fff'
});

// 分页参数
const pagination = reactive({
	page: 1,
	pageSize: 10,
	total: 0
});

const formData = reactive({
	id: null,
	name: "",
	username: "",
	password: "",
	disabled: null,
	is_superuser: null,
	avatar: "",
	description: "",
	created_at: "",
	updated_at: "",
});

// 初始化加载数据
onLoad(() => {
	fetchUserList();
});

// 获取用户列表
const fetchUserList = async () => {
	try {
		const params = {
			offset: (pagination.page - 1) * pagination.pageSize,
			limit: pagination.pageSize,
			name: searchQuery.value
		};

		const res = await list_user(params);

		if (pagination.page === 1) {
			tableData.value = res.data.items.map(item => ({
				...formData,
				...item
			}));
		} else {
			tableData.value = [...tableData.value, ...res.data.items.map(item => ({
				...formData,
				...item
			}))];
		}

		pagination.total = res.data.total;
		loadStatus.value = res.data.has_more ? 'more' : 'noMore';
	} catch (error) {
		console.error('获取用户列表失败:', error);
		uni.showToast({
			title: '获取用户列表失败',
			icon: 'none'
		});
	}
};

// 搜索用户
const handleSearch = () => {
	pagination.page = 1;
	fetchUserList();
};

// 加载更多
const loadMore = () => {
	if (loadStatus.value === 'more') {
		pagination.page++;
		fetchUserList();
	}
};

// 显示详情弹窗
const showDetailPopup = async (user) => {
	try {
		const res = await detail_user(user.id);
		currentDetail.value = res.data;
		popupTitle.value = `${res.data.id} - ${res.data.name}`;
		detailPopup.value.open();
	} catch (error) {
		console.error('获取用户详情失败:', error);
		uni.showToast({
			title: '获取用户详情失败',
			icon: 'none'
		});
	}
};

// 关闭详情弹窗
const closeDetailPopup = () => {
	detailPopup.value.close();
};

// 格式化字段标签
const formatLabel = (key) => {
	const labels = {
		id: 'ID',
		name: '用户名',
		username: '登录账号',
		disabled: '状态',
		is_superuser: '管理员类型',
		avatar: '头像',
		description: '描述',
		created_at: '创建时间',
		updated_at: '更新时间',
		password: '密码'
	};
	return labels[key] || key;
};

// 格式化字段值
const formatValue = (key, value) => {
	if (!value && value !== false) return '无';

	switch (key) {
		case 'disabled':
			return value ? '禁用' : '启用';
		case 'is_superuser':
			return value ? '超级管理员' : '普通用户';
		case 'created_at':
		case 'updated_at':
			return formatDate(value);
		default:
			return value;
	}
};

// 格式化日期
const formatDate = (dateString) => {
	if (!dateString) return '无';
	const date = new Date(dateString);
	return date.toLocaleString();
};
</script>

<style lang="scss" scoped>
.user-list-container {
	padding: 20rpx;
	background-color: #f5f5f5;
}

.search-area {
	display: flex;
	align-items: center;
	margin-bottom: 20rpx;
	background: #fff;
	border-radius: 16rpx;
	padding: 20rpx;
	box-shadow: 0 4rpx 12rpx rgba(0, 0, 0, 0.05);

	.search-input {
		flex: 1;
		margin-right: 20rpx;
	}
}

.avatar-wrapper {
	width: 80rpx;
	height: 80rpx;
	margin-right: 20rpx;

	.avatar {
		width: 100%;
		height: 100%;
		border-radius: 50%;
		background-color: #f0f0f0;
	}
}

/* 详情弹窗样式 */
.popup-content {
	width: 650rpx;
	background-color: #fff;
	border-radius: 16rpx;
	overflow: hidden;
}

.popup-header {
	display: flex;
	justify-content: space-between;
	align-items: center;
	padding: 30rpx;
	border-bottom: 1rpx solid #eee;
}

.popup-title {
	font-size: 32rpx;
	font-weight: bold;
	color: #333;
}

.popup-body {
	max-height: 800rpx;
	padding: 30rpx;
}

.detail-item {
	display: flex;
	margin-bottom: 20rpx;
	line-height: 1.6;
}

.detail-label {
	flex: 0 0 180rpx;
	color: #666;
	font-weight: bold;
}

.detail-value {
	flex: 1;
	color: #333;
	word-break: break-all;
}

.popup-footer {
	padding: 20rpx;
	display: flex;
	justify-content: center;
	border-top: 1rpx solid #eee;
}

.popup-button {
	width: 200rpx;
	background-color: #007aff;
	color: #fff;
}
</style>