<template>
	<view class="layout">
		<slot name="main"></slot>
	</view>

</template>

<script setup>

</script>

<style lang="scss">
.layout {
	min-height: (100vh - var(--status-bar-height));

	.main {
		padding: 20rpx;
	}
}
</style>