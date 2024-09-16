import request from "@/utils/request";

type TChangelog = {
  page: number;
  pageSize: number;
}

export const getDocsChangelog = async (searchParams : TChangelog) => {
  try {
    const res = await request.get("/api/admin/docs/changelog", {
      params: { page: searchParams.page, pageSize: searchParams.pageSize },
    });
    return res;
  } catch (error) {
    console.error(error);
  }
};
