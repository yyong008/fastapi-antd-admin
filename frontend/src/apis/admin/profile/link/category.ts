import request from "@/utils/request";

type TProfileLinkCategory = {
  page: number;
  pageSize: number;
}

export const getProfileLinkCategory = async (searchParams : TProfileLinkCategory) => {
  try {
    const res = await request.get("/api/admin/profile/link/category/", {
      params: { page: searchParams.page, pageSize: searchParams.pageSize },
    });
    return res;
  } catch (error) {
    console.error(error);
  }
};
