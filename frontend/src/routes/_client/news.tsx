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
    <section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
      <div className="mb-6">
        <h1 className="text-2xl font-semibold text-slate-900">News</h1>
        <p className="mt-2 text-sm text-slate-500">Latest updates and announcements.</p>
      </div>
      <div className="space-y-2">
        {news?.map((n: any) => {
          return <NewsItem data={n} key={n.id} />;
        })}
      </div>
    </section>
  );
}
