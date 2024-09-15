import request from "@/utils/request";

type TBlogTag = {
  page: number;
  pageSize: number;
}

export const getBlogTag = async (searchParams : TBlogTag) => {
  try {
    const res = await request.get("/api/admin/blog/tag", {
      params: { page: searchParams.page, size: searchParams.pageSize },
    });
    return res;
  } catch (error) {
    console.error(error);
  }
};
