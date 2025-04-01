<template>
	<view>
		<app-layout>

			<template #main>
				<view>
					<view class="search">
						<view class="search-input">
							<input type="text" placeholder="请输入用户名" v-model="formData.name" />
						</view>
						<view class="search-btn">
							<button type="primary" @click="handleList">搜索</button>
						</view>
					</view>
					<uni-table border stripe emptyText="暂无数据">
						<uni-tr>
							<uni-th width="15" align="center">ID</uni-th>
							<uni-th width="20" align="left">用户名</uni-th>
							<uni-th width="20" align="center">状态</uni-th>
						</uni-tr>
						<uni-tr v-for="item in tableData" :key="item.id">
							<uni-td align="center">{{ item.id }}</uni-td>
							<uni-td align="left">{{ item.name }}</uni-td>
							<uni-td align="center">{{ item.disabled ? '禁用' : '启用' }}</uni-td>
						</uni-tr>
					</uni-table>
					<uni-load-more :status="loadStatus" @clickLoadMore="loadMore" />
				</view>

			</template>

		</app-layout>
	</view>

</template>

<script setup>
import { ref } from "vue";
import { onReady } from "@dcloudio/uni-app";
import { list_user } from "../../api/apis";

// 增加注释，明确输入验证逻辑
const loadStatus = ref('more');
const formData = ref({
	id: null,
	name: "",
	username: "",
	password: "",
	disabled: null,
	is_superuser: null,
	avatar: "https://gw.alipayobjects.com/zos/rmsportal/BiazfanxmamNRoxxVxka.png",
	description: "",
	parent_id: null,
	created_at: "",
	updated_at: "",
});
const tableData = ref([]);
const pageData = ref({
	offset: 0,
	limit: 10,
	name: null,
});


// 加载数据
onReady(() => {
	handleList();
});

// 加载更多
function loadMore() {
	if (loadStatus.value === 'more') {
		pageData.value.page++;
		handleList();
	}
}

// 获取用户列表
async function handleList() {
	// 重置数据和分页
	tableData.value = [];
	pageData.value.offset = 0;
	
	const res = await list_user(pageData.value);
	console.log('用户列表', res);
	if (res.data.items.length === 0) {
		loadStatus.value = 'noMore';
		return;
	}
	tableData.value = tableData.value.concat(res.data.items);
	loadStatus.value = res.data.has_more ? 'more' : 'noMore';
}


</script>

<style lang="scss" scoped>
.search {
	display: flex;
	align-items: center;
	margin: 20rpx 0;
	padding: 0 20rpx;
	background: #fff;
	border-radius: 16rpx;
	box-shadow: 0 4rpx 12rpx rgba(0, 0, 0, 0.05);

	.search-input {
		flex: 1;
		margin-right: 20rpx;

		input {
			width: 100%;
			height: 80rpx;
			padding: 0 20rpx;
			border: none;
			border-radius: 8rpx;
			font-size: 28rpx;
		}
	}

	.search-btn {
		button {
			height: 80rpx;
			line-height: 80rpx;
			border-radius: 8rpx;
			font-size: 28rpx;
		}
	}
}

.uni-table {
	margin: 20rpx 0;
	background: #fff;
	border-radius: 16rpx;
	box-shadow: 0 4rpx 12rpx rgba(0, 0, 0, 0.05);

	.uni-tr {
		transition: all 0.2s ease;

		&:hover {
			background-color: #f5f5f5;
			transform: scale(1.01);
		}
	}
}
</style>