<template>
	<view>
		<app-layout>

			<template #main>
				<uni-table border stripe emptyText="暂无数据">
					<uni-tr>
						<uni-th width="15" align="center">ID</uni-th>
						<uni-th width="30" align="left">用户名</uni-th>
						<uni-th width="20" align="center">状态</uni-th>
					</uni-tr>
					<uni-tr v-for="item in userList" :key="item.id" @click="headDetail(item.id)">
						<uni-td align="center">{{ item.id }}</uni-td>
						<uni-td align="left">{{ item.name }}</uni-td>
						<uni-td align="center">{{ item.disabled ? '禁用' : '启用' }}</uni-td>
					</uni-tr>
				</uni-table>
				<uni-load-more :status="loadStatus" @clickLoadMore="loadMore" />
			</template>

		</app-layout>
	</view>

</template>

<script setup>
	import { ref } from "vue";
	import { onReady } from "@dcloudio/uni-app";
	import { list_user, detail_user } from "../../api/apis";

	// 增加注释，明确输入验证逻辑
	const loadStatus = ref('more');
	const userList = ref([]);
	const pageData = ref({
		offset: 0,
		limit: 10,
		name: null,
	});


	// 加载数据
	onReady(() => {
		handleList();
	});

	// 获取用户列表
	async function handleList() {
		list_user(pageData.value).then(res => {
			if (res.data.items.length === 0) {
				loadStatus.value = 'noMore';
				return;
			}	
			userList.value = userList.value.concat(res.data.items);
			loadStatus.value = res.data.has_more ? 'more' : 'noMore';
			uni.showToast({ title: res.message, icon: 'success' });
		});
	}

	// 加载更多
	function loadMore() {
		if (loadStatus.value === 'more') {
			pageData.value.page++;
			handleList();
		}
	}
	
	function headDetail(id) {
		// 跳转到详情页(预留)
		detail_user(id).then(res => {
			console.log('用户详情', res);
			uni.showToast({ title: res.message, icon:'success' });
		});
	}

</script>

<style lang="scss" scoped>

</style>