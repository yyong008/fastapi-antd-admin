import { NewsItem } from "@/components/Client/News/news-item";
import { createFileRoute } from "@tanstack/react-router";
import { getNewsList } from "@/apis/client/news";

export const Route = createFileRoute("/_client/news")({
  component: NewsRoute,
  loaderDeps: ({ search }: any) => ({
    page: search.page || 1,
    pageSize: search.pageSize || 10,
  }),
  async loader({ deps }) {
    const result: any = await getNewsList({
      page: deps.page,
      pageSize: deps.pageSize,
    });
    if (result && result.code === 0) {
      return result.data;
    }
  },
});

export function NewsRoute() {
  const data = Route.useLoaderData();
  const { list: news = [] } = data;
  return (
    <div className="flex flex-col pt-[140px] px-[20px] w-[70vw] min-h-[80vh]">
      <div>
        {news?.map((n: any) => {
          return <NewsItem data={n} key={n.id} />;
        })}
      </div>
      {/* <div>页数：{total}</div> */}
    </div>
  );
}
